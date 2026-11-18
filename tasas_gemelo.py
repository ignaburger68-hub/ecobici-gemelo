"""
tasas_gemelo.py - Cómo cambian las tasas del gemelo en el tiempo (y frente a lo observado)

Tres vistas, para las 30 estaciones sumadas o para una estación:
  1. A lo largo de un día: la tasa del modelo bloque a bloque (perfil base, mezcla con la
     ventana y tasa final con clima y factor del día) frente a los viajes observados, y la
     evolución del factor del día y del clima.
  2. La misma hora en distintos días: modelo, perfil base, mezcla y observado, día por día.
  3. Mapa de calor día x hora: viajes observados / viajes esperados por el modelo.

Todo se mide en "viajes en el bloque": tasa (viajes/hora) x minutos en que la estación
estuvo operativa con dato / 60. Así lo esperado y lo observado son comparables aunque falten
lecturas. Lo observado es kappa x eventos detectados en el feed (la misma corrección que usa
el modelo para los eventos del mismo minuto).

Cada tasa se calcula como la habría calculado el gemelo en ese momento: para el bloque que
empieza en t, con la información disponible hasta t (factor del día de la hora anterior).

Uso desde la terminal:  py -3.14 gemelo.py tasas --desde 2026-11-17 --hasta 2026-11-20
Lo usa también la pestaña "Tasas" de tablero.py.
"""
import os

import numpy as np
import pandas as pd

import config_gemelo as cfg
from datos_gemelo import bloque_de, es_habil

AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f4e79", "#c0392b", "#2e8b57", "#9a9a9a", "#d68910"
DIAS_CORTO = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
EVENTOS = {"ret": "retiros", "dev": "devoluciones"}


def _indices(gem, estacion):
    if estacion in (None, "", "todas"):
        return np.arange(gem.I)
    codes = list(gem.est["code"])
    if estacion not in codes:
        raise SystemExit(f"No conozco la estación {estacion}. Opciones: {', '.join(codes)}")
    return np.array([codes.index(estacion)])


def _limite(gem):
    """Último instante con lecturas: no se calculan tasas ni observados después."""
    u = gem.panel.ultima_lectura()
    return u if u is not None else pd.Timestamp.max


def bloques_desde(gem, t0, evento="ret", estacion=None, k_max=4):
    """
    Las tasas que usaría el gemelo en t0 para sus próximos bloques de 15 min (hasta k_max),
    sumadas sobre las estaciones elegidas, junto con lo observado en esos bloques.
    Devuelve una lista de dicts (uno por bloque).
    """
    P = gem.panel
    idx = _indices(gem, estacion)
    lam, mu, det, info = gem.tasas(t0)
    tasa = lam if evento == "ret" else mu
    cuenta = P.bret if evento == "ret" else P.bdev
    expo = P.bexr if evento == "ret" else P.bexd
    limite = _limite(gem)
    filas = []
    for k in range(min(k_max, tasa.shape[1])):
        s = pd.Timestamp(t0) + pd.Timedelta(minutes=15 * k)
        d, b = P.dia(s), bloque_de(s)
        if not (0 <= d < P.n_dias):
            continue
        dk = det.iloc[k * gem.I:(k + 1) * gem.I]
        base = dk[f"base_{evento}"].values
        w = dk[f"w_{evento}"].values
        vent = dk[f"vent_{evento}"].values
        mezcla = w * np.nan_to_num(vent) + (1 - w) * base
        termino = s + pd.Timedelta(minutes=15) <= limite
        mins = expo[:, d, b].astype(float) if termino else np.zeros(gem.I)
        m = mins[idx] / 60
        filas.append({
            "t": s, "dia": s.normalize(), "hora": s.hour, "minutos_con_dato": float(mins[idx].sum()),
            "observado": float((gem.kappa[idx] * cuenta[idx, d, b]).sum()) if termino else np.nan,
            "esperado_modelo": float((tasa[idx, k] * m).sum()),
            "esperado_base": float((base[idx] * m).sum()),
            "esperado_mezcla": float((mezcla[idx] * m).sum()),
            "tasa_modelo_h": float(tasa[idx, k].sum()),
            "tasa_base_h": float(base[idx].sum()),
            "tasa_mezcla_h": float(mezcla[idx].sum()),
            "factor_dia": float(dk[f"F_{evento}"].iloc[0]),
            "factor_clima": float(dk[f"clima_{evento}"].iloc[0]),
            "peso_ventana": float(np.average(w[idx], weights=np.maximum(base[idx], 1e-9))),
        })
    return filas


def serie_dia(gem, dia, evento="ret", estacion=None):
    """Vista 1: un bloque de 15 min por fila, de PRIMER_T0 a ULTIMO_T0 (sólo hasta la última lectura)."""
    dia = pd.Timestamp(dia).normalize()
    limite = _limite(gem)
    t0s = pd.date_range(dia + pd.Timedelta(cfg.PRIMER_T0 + ":00"), dia + pd.Timedelta(cfg.ULTIMO_T0 + ":00"),
                        freq="15min")
    filas = []
    for t in t0s[t0s <= limite]:
        filas += bloques_desde(gem, t, evento, estacion, k_max=1)
    return pd.DataFrame(filas)


def por_hora(gem, t_hora, evento="ret", estacion=None):
    """Suma de los 4 bloques de una hora, con las tasas calculadas al inicio de la hora (como el pronóstico)."""
    f = pd.DataFrame(bloques_desde(gem, t_hora, evento, estacion, k_max=4))
    if f.empty:
        return None
    sumas = ["observado", "esperado_modelo", "esperado_base", "esperado_mezcla", "minutos_con_dato"]
    out = {c: f[c].sum(min_count=1 if c == "observado" else 0) for c in sumas}
    if f["observado"].isna().any():
        out["observado"] = np.nan                       # la hora todavía no termina
    for c in ("tasa_modelo_h", "tasa_base_h", "tasa_mezcla_h", "factor_clima"):
        out[c] = f[c].mean()
    out.update(t=pd.Timestamp(t_hora), dia=pd.Timestamp(t_hora).normalize(), hora=pd.Timestamp(t_hora).hour,
               factor_dia=f["factor_dia"].iloc[0], peso_ventana=f["peso_ventana"].mean())
    return out


def dias_disponibles(gem, solo_habiles=False):
    limite = _limite(gem)
    dias = [d for d in gem.panel.fechas if d <= limite]
    if solo_habiles:
        dias = [d for d in dias if es_habil([d])[0]]
    return dias


def serie_hora(gem, hora="08:00", evento="ret", estacion=None, dias=None):
    """Vista 2: la misma hora en cada día."""
    dias = dias_disponibles(gem) if dias is None else dias
    filas = []
    for d in dias:
        r = por_hora(gem, pd.Timestamp(d) + pd.Timedelta(hora + ":00"), evento, estacion)
        if r is not None:
            r["habil"] = bool(es_habil([d])[0])
            filas.append(r)
    return pd.DataFrame(filas)


def mapa_calor(gem, evento="ret", estacion=None, dias=None, h_ini=6, h_fin=22, min_cobertura=0.5):
    """Vista 3: observado / esperado por día y hora. Celdas con poca cobertura del feed quedan vacías."""
    dias = dias_disponibles(gem) if dias is None else dias
    n_est = len(_indices(gem, estacion))
    filas = []
    for d in dias:
        for h in range(h_ini, h_fin + 1):
            r = por_hora(gem, pd.Timestamp(d) + pd.Timedelta(hours=h), evento, estacion)
            if r is None:
                continue
            cob = r["minutos_con_dato"] / (60 * n_est)
            ok = cob >= min_cobertura and np.isfinite(r["observado"]) and r["esperado_modelo"] > 0
            r["cobertura"] = cob
            r["razon"] = r["observado"] / r["esperado_modelo"] if ok else np.nan
            r["habil"] = bool(es_habil([d])[0])
            filas.append(r)
    return pd.DataFrame(filas)


# ---------------------------------------------------------------------
# Gráficos
# ---------------------------------------------------------------------
def _redondear(df, n=3):
    """round() sólo en las columnas numéricas (evita avisos de pandas con fechas)."""
    return df.assign(**{c: df[c].round(n) for c in df.select_dtypes("number").columns})


def _estilo(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e5e5e5", lw=0.8)
    ax.set_axisbelow(True)


def _etiqueta_dia(d):
    d = pd.Timestamp(d)
    extra = "" if es_habil([d])[0] else (" (festivo)" if d.dayofweek < 5 else "")
    return f"{DIAS_CORTO[d.dayofweek]} {d:%d/%m}{extra}"


def _titulo_estacion(gem, estacion):
    if estacion in (None, "", "todas"):
        return "30 estaciones"
    fila = gem.est[gem.est["code"] == estacion].iloc[0]
    return f"estación {estacion} {str(fila.get('nombre_corto', ''))[:30]}"


def figura_dia(gem, s, evento="ret", estacion=None):
    """Vista 1. Con una sola estación agrupa por hora (por bloque los conteos son muy pequeños)."""
    import matplotlib.pyplot as plt
    if s.empty:
        return None
    una = estacion not in (None, "", "todas")
    if una:
        g = s.assign(h=s["t"].dt.floor("h")).groupby("h")
        s = g[["observado", "esperado_modelo", "esperado_base", "esperado_mezcla"]].sum(min_count=1)
        s["factor_dia"] = g["factor_dia"].first()
        s["factor_clima"] = g["factor_clima"].mean()
        s = s.reset_index().rename(columns={"h": "t"})
        ancho, unidad, paso = 0.036, "viajes en la hora", pd.Timedelta(minutes=60)
    else:
        ancho, unidad, paso = 0.0088, "viajes en el bloque de 15 min", pd.Timedelta(minutes=15)
    s = s.assign(t=s["t"] + paso / 2)          # todo en el punto medio del periodo (barras y líneas alineadas)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True, gridspec_kw={"height_ratios": [3, 1.3]})
    a1.bar(s["t"], s["observado"], width=ancho, color=GRIS, alpha=0.55, label="Observado")
    a1.plot(s["t"], s["esperado_base"], color=VERDE, lw=1.2, ls="--", label="Perfil base")
    a1.plot(s["t"], s["esperado_mezcla"], color=NARANJA, lw=1.4, label="Base + ventana")
    a1.plot(s["t"], s["esperado_modelo"], color=AZUL, lw=2.2, label="Modelo (× clima × factor del día)")
    a1.set_ylabel(unidad)
    d = pd.Timestamp(s["t"].iloc[0])
    a1.set_title(f"{EVENTOS[evento].capitalize()} a lo largo del día · {_etiqueta_dia(d)} · "
                 f"{_titulo_estacion(gem, estacion)}", loc="left")
    a1.legend(frameon=False, fontsize=8, ncol=4, loc="upper left")
    _estilo(a1)
    a2.axhline(1, color="#bbbbbb", lw=0.8)
    a2.plot(s["t"], s["factor_dia"], color=ROJO, lw=1.8, label="Factor del día")
    a2.plot(s["t"], s["factor_clima"], color=AZUL, lw=1.4, ls=":", label="Factor de clima")
    a2.set_ylabel("multiplica la tasa")
    a2.legend(frameon=False, fontsize=8, ncol=2, loc="upper left")
    _estilo(a2)
    import matplotlib.dates as mdates
    a2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    fig.tight_layout()
    return fig


def figura_hora(gem, s, hora, evento="ret", estacion=None):
    """Vista 2."""
    import matplotlib.pyplot as plt
    if s.empty:
        return None
    x = np.arange(len(s))
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.bar(x, s["observado"], color=[GRIS if h else "#d9d9d9" for h in s["habil"]], alpha=0.8, label="Observado")
    ax.plot(x, s["esperado_base"], color=VERDE, lw=1.2, ls="--", marker="o", ms=3, label="Perfil base")
    ax.plot(x, s["esperado_mezcla"], color=NARANJA, lw=1.4, marker="o", ms=3, label="Base + ventana")
    ax.plot(x, s["esperado_modelo"], color=AZUL, lw=2.2, marker="o", ms=4, label="Modelo")
    ax.set_xticks(x, [_etiqueta_dia(d) for d in s["dia"]], rotation=0, fontsize=8)
    ax.set_ylabel("viajes en la hora")
    ax.set_title(f"{EVENTOS[evento].capitalize()} de {hora} a {int(hora[:2]) + 1:02d}{hora[2:]} en cada día · "
                 f"{_titulo_estacion(gem, estacion)}", loc="left")
    ax.legend(frameon=False, fontsize=8, ncol=4, loc="upper left")
    _estilo(ax)
    fig.tight_layout()
    return fig


def figura_mapa(gem, m, evento="ret", estacion=None):
    """Vista 3: razón observado / modelo, escala logarítmica centrada en 1."""
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    if m.empty or m["razon"].notna().sum() == 0:
        return None
    tabla = m.pivot_table(index="dia", columns="hora", values="razon", aggfunc="first")
    fig, ax = plt.subplots(figsize=(10, 0.45 * len(tabla) + 1.6))
    im = ax.imshow(tabla.values, cmap="RdBu_r", norm=LogNorm(vmin=0.5, vmax=2), aspect="auto")
    for i in range(tabla.shape[0]):
        for j in range(tabla.shape[1]):
            v = tabla.values[i, j]
            if np.isfinite(v):
                ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=7,
                        color="white" if (v > 1.5 or v < 0.65) else "#333333")
    ax.set_xticks(range(tabla.shape[1]), [f"{h:02d}" for h in tabla.columns], fontsize=8)
    ax.set_yticks(range(tabla.shape[0]), [_etiqueta_dia(d) for d in tabla.index], fontsize=8)
    ax.set_xlabel("hora del día (inicio)")
    ax.set_title(f"{EVENTOS[evento].capitalize()}: observado ÷ modelo · {_titulo_estacion(gem, estacion)}",
                 loc="left")
    cb = fig.colorbar(im, ax=ax, ticks=[0.5, 0.75, 1, 1.5, 2])
    cb.ax.set_yticklabels(["0,5", "0,75", "1", "1,5", "2"])
    from matplotlib.ticker import NullFormatter
    cb.ax.yaxis.set_minor_formatter(NullFormatter())
    cb.set_label("> 1: más viajes que lo esperado", fontsize=8)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------
# Comando "tasas" (lo llama gemelo.py)
# ---------------------------------------------------------------------
def comando_tasas(gem, desde, hasta, horas=("08:00", "13:00", "18:00"), estacion=None):
    import matplotlib.pyplot as plt
    c = os.path.join(cfg.CARPETA_RESULTADOS, "tasas" + (f"_{estacion}" if estacion not in (None, "", "todas") else ""))
    os.makedirs(c, exist_ok=True)
    dias = [d for d in dias_disponibles(gem) if pd.Timestamp(desde) <= d <= pd.Timestamp(hasta)]
    if not dias:
        raise SystemExit(f"No hay días con lecturas entre {desde} y {hasta}")
    print(f"Tasas de {len(dias)} días ({dias[0]:%d/%m} a {dias[-1]:%d/%m}) · {_titulo_estacion(gem, estacion)}")
    for ev in ("ret", "dev"):
        nombre = EVENTOS[ev]
        partes = []
        for d in dias:
            s = serie_dia(gem, d, ev, estacion)
            if s.empty:
                continue
            partes.append(s)
            fig = figura_dia(gem, s, ev, estacion)
            fig.savefig(os.path.join(c, f"dia_{d:%Y-%m-%d}_{nombre}.png"), dpi=120)
            plt.close(fig)
        if partes:
            _redondear(pd.concat(partes)).to_csv(os.path.join(c, f"bloques_{nombre}.csv"), index=False)
        for h in horas:
            s = serie_hora(gem, h, ev, estacion, dias)
            if s.empty:
                continue
            _redondear(s).to_csv(os.path.join(c, f"hora_{h.replace(':', '')}_{nombre}.csv"), index=False)
            fig = figura_hora(gem, s, h, ev, estacion)
            fig.savefig(os.path.join(c, f"hora_{h.replace(':', '')}_{nombre}.png"), dpi=120)
            plt.close(fig)
        m = mapa_calor(gem, ev, estacion, dias)
        if not m.empty:
            _redondear(m).to_csv(os.path.join(c, f"mapa_calor_{nombre}.csv"), index=False)
            fig = figura_mapa(gem, m, ev, estacion)
            if fig is not None:
                fig.savefig(os.path.join(c, f"mapa_calor_{nombre}.png"), dpi=120)
                plt.close(fig)
            r = m["razon"].dropna()
            if len(r):
                print(f"  {nombre}: observado ÷ modelo, mediana {r.median():.2f} "
                      f"(25 % de las horas bajo {r.quantile(0.25):.2f}, 25 % sobre {r.quantile(0.75):.2f})")
    print(f"Resultados en {c}")
    return c
