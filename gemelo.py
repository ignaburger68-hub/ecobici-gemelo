"""
gemelo.py - Gemelo digital de 30 estaciones Ecobici (programa principal)
Proyecto Simulación MIIIO/DIIIO 2-2026 · Tema 3 · Ignacio Chandia y Francisco Correa

Comandos (correr desde la carpeta con estaciones_seleccionadas.csv, los viajes y datos/):

  py -3.14 gemelo.py preparar
      Lee viajes, feed y clima, guarda la caché y muestra qué datos hay.

  py -3.14 gemelo.py hora "2026-11-26 07:45"
      Simulación de una hora desde ese instante (modo reproducción): pronóstico por
      estación, plan del camión, mapa, abanico y, como ya pasó, lo que efectivamente ocurrió.

  py -3.14 gemelo.py hora --en-vivo
      Lo mismo desde el estado actual del feed y el pronóstico del clima.

  py -3.14 gemelo.py validar --desde 2026-11-17 --hasta 2026-11-20
      Probabilidad simulada vs exacta (cadena de Markov) e histograma de saltos del feed.

  py -3.14 gemelo.py ajuste --desde 2026-11-17 --hasta 2026-11-20
      Elige W, m y phi por puntaje de Brier; guarda la tabla de persistencia.

  py -3.14 gemelo.py evaluar --desde 2026-11-23 --hasta 2026-11-27 [--planes]
      Gemelo vs sin resincronizar vs persistencia contra lo ocurrido; con --planes,
      también el valor de los planes de rebalanceo (sólo en simulación).

Opciones comunes: --R 1000 (réplicas). Todos los parámetros están en config_gemelo.py.
Semilla fija: cada pronóstico usa la semilla (SEMILLA, minuto de t0, uso), así que
cualquier resultado se reproduce exactamente.
"""
import argparse
import json
import os
import time

import numpy as np
import pandas as pd
import matplotlib

import config_gemelo as cfg
from datos_gemelo import DEMANDA_ES, TIPO_ES, es_habil, tabla_factores_clima, tipo_idx
from modelo_gemelo import Gemelo, delta_de, grupo_persistencia, tabla_persistencia

AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f4e79", "#c0392b", "#2e8b57", "#9a9a9a", "#d68910"
ARCHIVO_PERSISTENCIA = os.path.join(cfg.CARPETA_RESULTADOS, "persistencia.csv")
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


# =====================================================================
# Utilidades
# =====================================================================
def lista_t0(gem, desde, hasta):
    """Instantes de pronóstico: días hábiles con datos, cada 15 min de PRIMER_T0 a ULTIMO_T0."""
    out = []
    for d in pd.date_range(pd.Timestamp(desde).normalize(), pd.Timestamp(hasta).normalize()):
        if not es_habil([d])[0] or d not in gem.panel.fechas:
            continue
        if gem.panel.cobertura_dia[d] < cfg.MIN_COBERTURA_DIA:
            print(f"Aviso: {d:%Y-%m-%d} tiene poca cobertura del feed; se omite")
            continue
        out += list(pd.date_range(d + pd.Timedelta(cfg.PRIMER_T0 + ":00"), d + pd.Timedelta(cfg.ULTIMO_T0 + ":00"),
                                  freq=f"{cfg.PASO_T0_MIN}min"))
    if not out:
        raise SystemExit(f"No hay días hábiles con lecturas entre {desde} y {hasta}")
    return out


def carpeta(*partes):
    c = os.path.join(cfg.CARPETA_RESULTADOS, *partes)
    os.makedirs(c, exist_ok=True)
    return c


def leer_persistencia():
    if os.path.isfile(ARCHIVO_PERSISTENCIA):
        return pd.read_csv(ARCHIVO_PERSISTENCIA)
    return None


def p_persistencia(pers, B0, D0):
    """Probabilidad de persistencia (tabla del ajuste) y versión 0/1."""
    v01 = (B0 == 0).astype(float)
    l01 = (D0 == 0).astype(float)
    if pers is None:
        return v01, l01, v01, l01
    pv = pers.set_index("grupo")["p_vacia"].reindex(grupo_persistencia(B0)).fillna(0).values
    pl = pers.set_index("grupo")["p_llena"].reindex(grupo_persistencia(D0)).fillna(0).values
    return pv, pl, v01, l01


def estilo(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.3)


# =====================================================================
# Simulación de una hora (el entregable)
# =====================================================================
def simulacion_una_hora(gem, t0=None, en_vivo=False, R=None, guardar=True, con_referencias=True,
                        estado=None, carpeta_salida=None):
    import matplotlib.pyplot as plt
    R = cfg.R if R is None else R
    if estado is not None:
        t0 = pd.Timestamp(t0)
    elif en_vivo:
        t0, estado = gem.estado_vivo()
        print(f"Estado en vivo leído a las {t0:%H:%M}")
    else:
        t0 = pd.Timestamp(t0)
        estado = gem.estado(t0)
    inicio = time.time()
    pron = gem.pronosticar(t0, R=R, estado=estado, minutos=True)
    pron0 = gem.pronosticar(t0, R=R, estado=estado, usar_phi=False, uso=5)       # para validar
    pv_ex, pl_ex = gem.exactas(pron0)
    plan = gem.planificar(pron)
    obs = None if en_vivo else gem.observado(t0)
    ultima = gem.panel.ultima_lectura()
    if obs is not None and (ultima is None or t0 + pd.Timedelta(minutes=60) > ultima):
        obs = None          # la hora todavía no termina en los datos: no hay "lo que ocurrió"
    est, e = gem.est, pron["estado"]

    tabla = pd.DataFrame({
        "code": est["code"], "nombre": est["nombre_corto"], "perfil": est["perfil"],
        "B_t0": np.where(e["ok"], e["B0"], np.nan), "C": np.where(e["ok"], e["C"], np.nan),
        "retiros_h": pron["lam"].mean(1).round(2), "devoluciones_h": pron["mu"].mean(1).round(2),
        "p_vacia": pron["p_vac"].round(3), "p_llena": pron["p_lle"].round(3),
        "p_vacia_exacta_sin_phi": np.round(pv_ex, 3), "p_vacia_sim_sin_phi": pron0["p_vac_cont"].round(3),
        "p_llena_exacta_sin_phi": np.round(pl_ex, 3), "p_llena_sim_sin_phi": pron0["p_lle_cont"].round(3),
        "B_t60_mediana": pron["q50"], "B_t60_ic80": [f"{a:.0f}-{b:.0f}" if np.isfinite(a) else ""
                                                    for a, b in zip(pron["q10"], pron["q90"])],
        "B_t60_ic90": [f"{a:.0f}-{b:.0f}" if np.isfinite(a) else "" for a, b in zip(pron["q05"], pron["q95"])],
        "min_vacia_esp": pron["min_vac"].round(1), "min_llena_esp": pron["min_lle"].round(1),
        "retiros_perdidos_esp": pron["perdidos"].round(2), "devol_rechazadas_esp": pron["rechazados"].round(2),
    })
    delta_v = delta_de(plan["planes"]["Gemelo (voraz)"], gem.I)
    tabla["cambio_plan_gemelo"] = delta_v
    G = plan["G"]
    sin = np.array([G[i, e["B0"][i]] if e["ok"][i] else np.nan for i in range(gem.I)])
    con = np.array([G[i, e["B0"][i] + delta_v[i]] if e["ok"][i] else np.nan for i in range(gem.I)])
    tabla["no_atendida_sin_accion"] = sin.round(2)
    tabla["no_atendida_con_plan"] = con.round(2)

    brier = None
    if obs is not None:
        tabla["vacia_real"] = np.where(obs["ok"], obs["y_vac"], np.nan)
        tabla["llena_real"] = np.where(obs["ok"], obs["y_lle"], np.nan)
        tabla["B_t60_real"] = obs["B60"]
        tabla["camion_operador"] = obs["camion"]
        if con_referencias:
            modelos = {"Gemelo": (pron["p_vac"], pron["p_lle"])}
            if t0.hour >= 6 and es_habil([t0])[0]:
                ps = gem.pron_sin_resinc(gem.sin_resincronizar_dia(t0.normalize(), R=R), t0)
                modelos["Sin resincronizar"] = (ps["p_vac"], ps["p_lle"])
                tabla["p_vacia_sin_resinc"] = ps["p_vac"].round(3)
                tabla["p_llena_sin_resinc"] = ps["p_lle"].round(3)
            pv, pl, v01, l01 = p_persistencia(leer_persistencia(), e["B0"], e["C"] - e["B0"])
            modelos["Persistencia"] = (pv, pl)
            modelos["Persistencia 0/1"] = (v01, l01)
            val = obs["ok"] & e["ok"] & ~obs["camion"]
            filas = []
            for n, (a, b) in modelos.items():
                bv = np.nanmean((a[val] - obs["y_vac"][val]) ** 2)
                bl = np.nanmean((b[val] - obs["y_lle"][val]) ** 2)
                filas.append({"modelo": n, "brier_vacia": bv, "brier_llena": bl, "estaciones": int(val.sum())})
            brier = pd.DataFrame(filas)

    res = {"t0": t0, "tabla": tabla, "pron": pron, "plan": plan, "obs": obs, "brier": brier,
           "en_vivo": en_vivo, "segundos": time.time() - inicio}
    res["clima"] = clima_de_la_hora(gem, t0, pron["detalle"])
    res["fig_mapa"] = figura_mapa(gem, res)
    res["fig_abanico"] = figura_abanico(gem, res)
    res["texto"] = texto_hora(gem, res)
    if guardar:
        if carpeta_salida:
            c = carpeta_salida
            os.makedirs(c, exist_ok=True)
        else:
            c = carpeta(f"hora_{t0:%Y-%m-%d_%H%M}" + ("_vivo" if en_vivo else ""))
        tabla.to_csv(os.path.join(c, "pronostico_estaciones.csv"), index=False)
        plan["traslados"].to_csv(os.path.join(c, "plan_traslados.csv"), index=False)
        plan["comparacion"].round(3).to_csv(os.path.join(c, "comparacion_planes.csv"), index=False)
        pron["detalle"].round(3).to_csv(os.path.join(c, "detalle_tasas.csv"), index=False)
        if brier is not None:
            brier.round(4).to_csv(os.path.join(c, "brier_esta_hora.csv"), index=False)
        tabla_clima(res["clima"]).to_csv(os.path.join(c, "clima.csv"), index=False)
        res["fig_mapa"].savefig(os.path.join(c, "mapa.png"), dpi=130)
        res["fig_abanico"].savefig(os.path.join(c, "abanico.png"), dpi=130)
        with open(os.path.join(c, "resumen.txt"), "w", encoding="utf-8") as fh:
            fh.write(res["texto"])
        plt.close("all")
        res["carpeta"] = c
    return res


# ---------------------------------------------------------------------
# Clima de la hora simulada y cómo cambia la demanda
# ---------------------------------------------------------------------
VARIABLES_CLIMA = [("lluvia", "lluvia_cat"), ("lluvia previa", "previa_cat"),
                   ("temperatura", "temp_cat"), ("viento", "viento_cat")]


def _num(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return np.nan
    return x if np.isfinite(x) else np.nan


def clima_de_la_hora(gem, t0, detalle=None):
    """
    Clima de la hora que cubre la mayor parte de [t0, t0+60) (la misma tabla por hora que usa el modelo) y su efecto:
    para cada variable, la categoría y el factor de resultados_clima/factores_clima_gemelo.csv;
    el efecto aplicado es el producto de los cuatro factores (promedio de los 4 bloques de 15 min).
    """
    t0 = pd.Timestamp(t0)
    h = (t0 + pd.Timedelta(minutes=30)).floor("h")   # la hora que cubre la mayor parte de la simulación
    t = tipo_idx(t0)
    # Si la hora todavía no termina, el clima es el pronóstico meteorológico (no puede ser lo registrado)
    fuente = "pronosticado" if h + pd.Timedelta(hours=1) > ahora_local() else "registrado"
    out = {"hora": h, "tipo_dia": TIPO_ES[t], "hay_dato": False, "factores": None, "fuente": fuente,
           "efecto_ret": 1.0, "efecto_dev": 1.0}
    if detalle is not None and len(detalle) and "clima_ret" in detalle:
        out["efecto_ret"] = float(detalle.drop_duplicates("bloque")["clima_ret"].mean())
        out["efecto_dev"] = float(detalle.drop_duplicates("bloque")["clima_dev"].mean())
    else:
        out["efecto_ret"], out["efecto_dev"] = gem.fc(t0, t, "ret"), gem.fc(t0, t, "dev")
    c = gem.clima
    if c is None or h not in c.index or not np.isfinite(_num(c.loc[h, "temperatura_c"])):
        return out
    r = c.loc[h]
    out.update(hay_dato=True, temperatura_c=_num(r["temperatura_c"]), temp_dif_c=_num(r.get("temp_dif_c")),
               precipitacion_mm=_num(r["precipitacion_mm"]), lluvia_previa_mm=_num(r.get("lluvia_previa_mm")),
               viento_kmh=_num(r["viento_kmh"]))
    tabla = tabla_factores_clima()
    filas = []
    for var, col in VARIABLES_CLIMA:
        cat = r.get(col)
        cat = cat if isinstance(cat, str) else "sin dato"
        filas.append({"variable": var, "categoria": cat,
                      "factor_retiros": tabla.get((TIPO_ES[t], DEMANDA_ES["ret"], var, cat), 1.0),
                      "factor_devoluciones": tabla.get((TIPO_ES[t], DEMANDA_ES["dev"], var, cat), 1.0)})
    out["factores"] = pd.DataFrame(filas)
    return out


def _pct(f):
    return f"×{f:.2f} ({100 * (f - 1):+.0f} %)"


def lineas_clima(cl):
    """Texto corto del clima de la hora y su efecto (para resumen.txt, la terminal y el tablero)."""
    h = cl["hora"]
    L = []
    if cl["hay_dato"]:
        dif = cl["temp_dif_c"]
        dif_txt = f" ({dif:+.1f} °C respecto de lo normal a esa hora)" if np.isfinite(dif) else ""
        ll = cl["precipitacion_mm"]
        ll_txt = "sin dato de lluvia" if not np.isfinite(ll) else ("sin lluvia" if ll < cfg.UMBRAL_LLUVIA
                                                                     else f"lluvia {ll:.1f} mm/h")
        L.append(f"Clima {cl['fuente']} de {h:%H:%M} a {h + pd.Timedelta(hours=1):%H:%M} (día {cl['tipo_dia']}): "
                 f"{cl['temperatura_c']:.1f} °C{dif_txt}, {ll_txt}, viento {cl['viento_kmh']:.0f} km/h")
    else:
        L.append(f"Clima {cl['fuente']} de {h:%H:%M} a {h + pd.Timedelta(hours=1):%H:%M}: sin datos "
                 "(el clima se toma como normal)")
    L.append(f"Efecto del clima en la hora: retiros {_pct(cl['efecto_ret'])}, "
             f"devoluciones {_pct(cl['efecto_dev'])}  (×1,00 = sin efecto)")
    if cl["factores"] is not None:
        for _, f in cl["factores"].iterrows():
            L.append(f"  {f['variable']:<14} {f['categoria']:<30} retiros ×{f['factor_retiros']:.3f}  "
                     f"devoluciones ×{f['factor_devoluciones']:.3f}")
    return L


def tabla_clima(cl):
    """Tabla para guardar (clima.csv): una fila por variable y una fila final con el efecto total."""
    base = {"hora": f"{cl['hora']:%Y-%m-%d %H:%M}", "tipo_dia": cl["tipo_dia"], "fuente": cl["fuente"],
            "temperatura_c": cl.get("temperatura_c", np.nan), "temp_dif_c": cl.get("temp_dif_c", np.nan),
            "precipitacion_mm": cl.get("precipitacion_mm", np.nan), "viento_kmh": cl.get("viento_kmh", np.nan)}
    filas = [] if cl["factores"] is None else [dict(base, **f) for f in cl["factores"].to_dict("records")]
    filas.append(dict(base, variable="efecto total en la hora", categoria="",
                      factor_retiros=cl["efecto_ret"], factor_devoluciones=cl["efecto_dev"]))
    return pd.DataFrame(filas).round(3)


def texto_hora(gem, res):
    t0, tabla, plan, pron = res["t0"], res["tabla"], res["plan"], res["pron"]
    info = pron["info"]
    L = [f"Simulación de una hora — {DIAS[t0.dayofweek]} {t0:%d/%m/%Y} {t0:%H:%M} a "
         f"{t0 + pd.Timedelta(minutes=60):%H:%M}"
         + (" (en vivo)" if res["en_vivo"] else " (reproducción)"),
         f"Réplicas: {pron['R']} · phi = {pron['phi']} · ventana: {', '.join(info['dias_ventana']) or 'sin ventana'}",
         f"Factor del día: retiros {info['F']['ret']:.2f}, devoluciones {info['F']['dev']:.2f}",
         f"Estaciones con dato: {int(np.isfinite(tabla['p_vacia']).sum())} de {len(tabla)}", ""]
    if res.get("clima") is not None:
        L += lineas_clima(res["clima"]) + [""]
    t = tabla.assign(riesgo=np.fmax(tabla["p_vacia"], tabla["p_llena"])).sort_values("riesgo", ascending=False)
    L.append("Estaciones con más riesgo:")
    for _, r in t.head(8).iterrows():
        L.append(f"  {r['code']:>8} {str(r['nombre'])[:26]:<26} B={r['B_t0']:.0f}/{r['C']:.0f}  "
                 f"p vacía {r['p_vacia']:.2f}  p llena {r['p_llena']:.2f}  B(t+60) {r['B_t60_ic80']}")
    L.append("")
    for nombre in ("Regla umbral", "Gemelo (voraz)"):
        L.append(f"Plan {nombre}:")
        tr = plan["traslados"]
        tr = tr[tr["plan"] == nombre] if len(tr) else tr
        if len(tr) == 0:
            L.append("  sin traslados")
        for _, r in tr.iterrows():
            L.append(f"  {r['orden']}. llevar {r['bicis']} bicis de {r['origen']} ({r['B_origen']}/{r['C_origen']}) "
                     f"a {r['destino']} ({r['B_destino']}/{r['C_destino']})")
    L.append("")
    L.append("Demanda no atendida esperada en la hora (30 estaciones, réplicas nuevas y comunes a los planes):")
    for _, r in plan["comparacion"].iterrows():
        L.append(f"  {r['plan']:<38} {r['no_atendida_media']:6.1f}  "
                 f"(atiende {r['atendidos_extra_vs_sin_accion']:+.1f} vs sin acción, "
                 f"IC95 {r['dif_ic95_inf']:+.1f} a {r['dif_ic95_sup']:+.1f})")
    if res["brier"] is not None:
        L.append("")
        L.append("Lo que ocurrió (puntaje de Brier de esta hora, sin estaciones con camión del operador):")
        for _, r in res["brier"].iterrows():
            L.append(f"  {r['modelo']:<20} vacía {r['brier_vacia']:.3f}   llena {r['brier_llena']:.3f}")
        tv = tabla.dropna(subset=["vacia_real"])
        L.append(f"  Estaciones que quedaron vacías: {int(tv['vacia_real'].sum())}, llenas: "
                 f"{int(tv['llena_real'].sum())}, con camión del operador: {int(tabla['camion_operador'].sum())}")
    ex = tabla.dropna(subset=["p_vacia_exacta_sin_phi"])
    if len(ex):
        d = np.abs(np.r_[ex["p_vacia_exacta_sin_phi"] - ex["p_vacia_sim_sin_phi"],
                         ex["p_llena_exacta_sin_phi"] - ex["p_llena_sim_sin_phi"]])
        L.append("")
        L.append(f"Validación: |simulada − exacta| máx {d.max():.3f}, media {d.mean():.3f} "
                 f"(error de Monte Carlo ≈ {0.5 / np.sqrt(pron['R']):.3f})")
    L.append(f"\nTiempo de cálculo: {res['segundos']:.1f} s")
    return "\n".join(L) + "\n"


def figura_mapa(gem, res):
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    tabla, plan = res["tabla"], res["plan"]
    fig, ax = plt.subplots(figsize=(9, 8))
    x, y = gem.lon, gem.lat
    riesgo = (tabla["p_llena"] - tabla["p_vacia"]).values
    tam = 60 + 500 * np.nan_to_num(np.fmax(tabla["p_vacia"], tabla["p_llena"]).values)
    sc = ax.scatter(x, y, c=np.nan_to_num(riesgo), cmap="RdBu", vmin=-1, vmax=1, s=tam,
                    edgecolor="k", lw=0.6, zorder=3)
    for i, c in enumerate(tabla["code"]):
        b, cap = tabla["B_t0"][i], tabla["C"][i]
        txt = f"{c}\n{b:.0f}/{cap:.0f}" if np.isfinite(b) else f"{c}\nsin dato"
        ax.annotate(txt, (x[i], y[i]), fontsize=6.5, xytext=(6, 4), textcoords="offset points")
    for nombre, color, ls in [("Regla umbral", GRIS, "--"), ("Gemelo (voraz)", VERDE, "-")]:
        for o, d, q, _ in plan["planes"][nombre]:
            ax.annotate("", xy=(x[d], y[d]), xytext=(x[o], y[o]),
                        arrowprops=dict(arrowstyle="-|>", color=color, lw=2.2, ls=ls), zorder=4)
            ax.text((x[o] + x[d]) / 2, (y[o] + y[d]) / 2, f"{q}", color=color, fontsize=9, fontweight="bold")
    cb = fig.colorbar(sc, ax=ax, shrink=0.6)
    cb.set_label("← riesgo de quedar vacía · riesgo de quedar llena →")
    ax.set_aspect(1 / np.cos(np.radians(np.nanmean(y))))
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    t0 = res["t0"]
    ax.set_title(f"Pronóstico {t0:%d/%m/%Y %H:%M} a {t0 + pd.Timedelta(minutes=60):%H:%M}\n"
                 "Tamaño: probabilidad mayor; etiqueta: código y bicis/capacidad ahora", loc="left", fontsize=10)
    ax.legend(handles=[Line2D([], [], color=VERDE, lw=2, label="Plan del gemelo"),
                       Line2D([], [], color=GRIS, lw=2, ls="--", label="Regla umbral")],
              loc="lower left", fontsize=8)
    fig.tight_layout()
    return fig


def figura_abanico(gem, res, n=6):
    import matplotlib.pyplot as plt
    tabla, pron, obs = res["tabla"], res["pron"], res["obs"]
    st = pron["st_min"]
    e = pron["estado"]
    riesgo = np.nan_to_num(np.fmax(tabla["p_vacia"], tabla["p_llena"]).values, nan=-1)
    # primero las que todavía no están vacías ni llenas (ahí el pronóstico informa algo)
    en_extremo = (e["B0"] == 0) | (e["B0"] == e["C"])
    riesgo = np.where(en_extremo, riesgo - 2, riesgo)
    elegidas = np.argsort(-riesgo)[:n]
    fig, axs = plt.subplots(2, 3, figsize=(13, 6.5), sharex=True)
    m = np.arange(0, 61)
    for ax, i in zip(axs.ravel(), elegidas):
        tray = np.concatenate([np.full((st.shape[1], 1), e["B0"][i]), st[i]], axis=1).astype(float)
        q = np.percentile(tray, [5, 25, 50, 75, 95], axis=0)
        ax.fill_between(m, q[0], q[4], color=AZUL, alpha=0.15, label="90 % de las réplicas")
        ax.fill_between(m, q[1], q[3], color=AZUL, alpha=0.3, label="50 %")
        ax.plot(m, q[2], color=AZUL, lw=1.5, label="mediana")
        if obs is not None:
            real = np.r_[e["B0"][i], obs["trayectoria"][i]]
            ax.step(m, real, where="post", color="k", lw=1.4, label="lo que ocurrió")
        ax.axhline(0, color=ROJO, lw=1, ls=":")
        ax.axhline(e["C"][i], color=AZUL, lw=1, ls=":")
        ax.set_ylim(-0.5, e["C"][i] + 0.5)
        ax.set_title(f"{tabla['code'][i]} · {str(tabla['nombre'][i])[:22]}\n"
                     f"p vacía {tabla['p_vacia'][i]:.2f} · p llena {tabla['p_llena'][i]:.2f}", fontsize=9, loc="left")
        estilo(ax)
    for ax in axs[-1]:
        ax.set_xlabel("Minutos desde t0")
    for ax in axs[:, 0]:
        ax.set_ylabel("Bicis disponibles")
    axs[0, 0].legend(fontsize=7, frameon=False)
    fig.suptitle(f"Las {n} estaciones con más riesgo — {res['t0']:%d/%m/%Y %H:%M} (sin acción)", x=0.01, ha="left")
    fig.tight_layout()
    return fig


# =====================================================================
# Validación
# =====================================================================
def validar(gem, desde, hasta, n_horas=40, R=None):
    import matplotlib.pyplot as plt
    R = cfg.R if R is None else R
    t0s = lista_t0(gem, desde, hasta)
    rng = np.random.default_rng(cfg.SEMILLA)
    elegidos = sorted(rng.choice(len(t0s), size=min(n_horas, len(t0s)), replace=False))
    filas = []
    for k, j in enumerate(elegidos):
        t0 = t0s[j]
        pron = gem.pronosticar(t0, R=R, usar_phi=False, uso=5)
        pv, pl = gem.exactas(pron)
        for i in np.flatnonzero(pron["estado"]["ok"]):
            filas.append({"t0": t0, "code": gem.est["code"][i], "evento": "vacía",
                          "simulada": pron["p_vac_cont"][i], "exacta": pv[i]})
            filas.append({"t0": t0, "code": gem.est["code"][i], "evento": "llena",
                          "simulada": pron["p_lle_cont"][i], "exacta": pl[i]})
        if k % 10 == 0:
            print(f"Validación: {k + 1} de {len(elegidos)} horas")
    v = pd.DataFrame(filas)
    v["ee"] = np.sqrt(np.clip(v["exacta"] * (1 - v["exacta"]), 1e-12, None) / R)
    v["dentro_2ee"] = np.abs(v["simulada"] - v["exacta"]) <= 2 * v["ee"] + 1e-9
    c = carpeta("validacion")
    v.to_csv(os.path.join(c, "simulada_vs_exacta.csv"), index=False)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4.8))
    for ax, ev in zip(axs[:2], ["vacía", "llena"]):
        s = v[v["evento"] == ev]
        ax.errorbar(s["exacta"], s["simulada"], yerr=2 * s["ee"], fmt="o", ms=3, alpha=0.5, color=AZUL, elinewidth=0.6)
        ax.plot([0, 1], [0, 1], color="k", lw=0.8)
        ax.set_xlabel("Probabilidad exacta (cadena de Markov)")
        ax.set_ylabel("Probabilidad simulada")
        ax.set_title(f"Quedar {ev}: {s['dentro_2ee'].mean():.1%} dentro de ±2 errores estándar", loc="left")
        estilo(ax)
    s = gem.panel.saltos
    if len(s):
        lim = max(10, int(np.percentile(np.abs(s), 99.9)) + 1)
        bins = np.arange(-lim - 0.5, lim + 1.5)
        axs[2].hist(np.clip(s, -lim, lim), bins=bins, color=GRIS)
        axs[2].set_yscale("log")
        for u in (-cfg.UMBRAL_CAMION - 0.5, cfg.UMBRAL_CAMION + 0.5):
            axs[2].axvline(u, color=ROJO, ls="--")
        axs[2].set_title(f"Saltos entre reportes del feed (umbral camión ±{cfg.UMBRAL_CAMION})", loc="left")
        axs[2].set_xlabel("Cambio de bicis entre dos reportes")
        estilo(axs[2])
    fig.tight_layout()
    fig.savefig(os.path.join(c, "validacion.png"), dpi=130)
    texto = (f"Validación del simulador ({len(elegidos)} horas, {R} réplicas, sin phi)\n"
             + "\n".join(f"  {ev}: {g['dentro_2ee'].mean():.1%} dentro de ±2 EE; |dif| media "
                         f"{np.abs(g['simulada'] - g['exacta']).mean():.4f}, máx {np.abs(g['simulada'] - g['exacta']).max():.4f}"
                         for ev, g in v.groupby("evento")))
    with open(os.path.join(c, "validacion.txt"), "w", encoding="utf-8") as fh:
        fh.write(texto + "\n")
    print(texto)
    print(f"Resultados en {c}")
    return v


# =====================================================================
# Ajuste
# =====================================================================
def ajuste(gem, desde, hasta, R=None):
    R = cfg.R_AJUSTE if R is None else R
    t0s = lista_t0(gem, desde, hasta)
    print(f"Ajuste: {len(t0s)} pronósticos por combinación, "
          f"{len(cfg.GRILLA_W) * len(cfg.GRILLA_M) * len(cfg.GRILLA_PHI)} combinaciones, {R} réplicas")
    obs, est0 = {}, {}
    for t0 in t0s:
        o = gem.observado(t0)
        if o is not None:
            obs[t0] = o
            est0[t0] = gem.estado(t0)
    filas = []
    for W in cfg.GRILLA_W:
        for m in cfg.GRILLA_M:
            for phi in cfg.GRILLA_PHI:
                ev_v, ev_l = [], []
                inicio = time.time()
                for t0, o in obs.items():
                    p = gem.pronosticar(t0, R=R, W=W, m=m, usar_phi=phi, estado=est0[t0])
                    val = o["ok"] & est0[t0]["ok"] & ~o["camion"]
                    ev_v.append((p["p_vac"][val] - o["y_vac"][val]) ** 2)
                    ev_l.append((p["p_lle"][val] - o["y_lle"][val]) ** 2)
                bv, bl = np.concatenate(ev_v).mean(), np.concatenate(ev_l).mean()
                filas.append({"W": W, "m": m, "usar_phi": phi, "brier_vacia": bv, "brier_llena": bl,
                              "brier_promedio": (bv + bl) / 2, "n": len(np.concatenate(ev_v))})
                print(f"  W={W:>2} m={m:>2} phi={'sí' if phi else 'no'}: Brier vacía {bv:.4f}, llena {bl:.4f} "
                      f"({time.time() - inicio:.0f} s)")
    tab = pd.DataFrame(filas).sort_values("brier_promedio")
    c = carpeta()
    tab.round(5).to_csv(os.path.join(c, "ajuste_resultados.csv"), index=False)
    mejor = tab.iloc[0]
    par = {"W": int(mejor["W"]), "m": int(mejor["m"]), "usar_phi": bool(mejor["usar_phi"]),
           "brier_promedio": float(mejor["brier_promedio"]), "ajuste_desde": str(desde), "ajuste_hasta": str(hasta)}
    with open(cfg.ARCHIVO_PARAMETROS, "w", encoding="utf-8") as fh:
        json.dump(par, fh, indent=2)
    gem.params.update({k: par[k] for k in ("W", "m", "usar_phi")})

    # Persistencia probabilística con los mismos días
    B0 = np.concatenate([est0[t]["B0"][o["ok"] & est0[t]["ok"]] for t, o in obs.items()])
    D0 = np.concatenate([(est0[t]["C"] - est0[t]["B0"])[o["ok"] & est0[t]["ok"]] for t, o in obs.items()])
    yv = np.concatenate([o["y_vac"][o["ok"] & est0[t]["ok"]] for t, o in obs.items()])
    yl = np.concatenate([o["y_lle"][o["ok"] & est0[t]["ok"]] for t, o in obs.items()])
    pers = tabla_persistencia(B0, D0, yv, yl)
    pers.to_csv(ARCHIVO_PERSISTENCIA, index=False)
    print("\n" + tab.round(4).to_string(index=False))
    print(f"\nElegido: W = {par['W']}, m = {par['m']}, phi = {'sí' if par['usar_phi'] else 'no'} "
          f"-> {cfg.ARCHIVO_PARAMETROS}")
    print("Persistencia (frecuencia de quedar vacía / llena en la hora siguiente):")
    print(pers.round(3).to_string(index=False))
    return tab


# =====================================================================
# Evaluación
# =====================================================================
def evaluar(gem, desde, hasta, con_planes=False, R=None):
    R = cfg.R if R is None else R
    t0s = lista_t0(gem, desde, hasta)
    pers = leer_persistencia()
    if pers is None:
        print("Aviso: no hay tabla de persistencia (corre 'ajuste' primero); se usa sólo la versión 0/1")
    print(f"Evaluación: {len(t0s)} pronósticos · W = {gem.params['W']}, m = {gem.params['m']}, "
          f"phi = {'sí' if gem.params['usar_phi'] else 'no'}")
    filas, planes = [], []
    sr, dia_sr = None, None
    inicio = time.time()
    for k, t0 in enumerate(t0s):
        o = gem.observado(t0)
        if o is None:
            continue
        if dia_sr != t0.normalize():
            dia_sr = t0.normalize()
            sr = gem.sin_resincronizar_dia(dia_sr, R=R)
            print(f"  {DIAS[dia_sr.dayofweek]} {dia_sr:%d/%m}: {time.time() - inicio:.0f} s")
        p = gem.pronosticar(t0, R=R)
        ps = gem.pron_sin_resinc(sr, t0)
        e = p["estado"]
        pv, pl, v01, l01 = p_persistencia(pers, e["B0"], e["C"] - e["B0"])
        filas.append(pd.DataFrame({
            "t0": t0, "fecha": t0.normalize(), "hora": t0.hour + t0.minute / 60, "code": gem.est["code"],
            "ok": o["ok"] & e["ok"], "camion": o["camion"], "B0": e["B0"], "C": e["C"],
            "y_vac": o["y_vac"].astype(int), "y_lle": o["y_lle"].astype(int), "B60": o["B60"],
            "p_vac_gemelo": p["p_vac"], "p_lle_gemelo": p["p_lle"],
            "p_vac_sin_resinc": ps["p_vac"], "p_lle_sin_resinc": ps["p_lle"],
            "p_vac_persist": pv, "p_lle_persist": pl, "p_vac_persist01": v01, "p_lle_persist01": l01,
            "q05": p["q05"], "q10": p["q10"], "q50": p["q50"], "q90": p["q90"], "q95": p["q95"],
            "sr_q10": ps["q10"], "sr_q50": ps["q50"], "sr_q90": ps["q90"]}))
        if con_planes:
            pl_ = gem.planificar(p, tiempos=True)
            planes.append(pl_["comparacion"].assign(t0=t0))
    df = pd.concat(filas, ignore_index=True)
    c = carpeta("evaluacion")
    df.to_csv(os.path.join(c, "pronosticos_evaluacion.csv"), index=False)
    dp = pd.concat(planes, ignore_index=True) if planes else None
    if dp is not None:
        dp.to_csv(os.path.join(c, "planes_evaluacion.csv"), index=False)
    print(f"Pronósticos listos ({time.time() - inicio:.0f} s). Calculando métricas...")
    return informe(df, dp, c)


MODELOS = {"Gemelo": "gemelo", "Sin resincronizar": "sin_resinc", "Persistencia": "persist",
           "Persistencia 0/1": "persist01"}


def tabla_umbrales(val, umbrales=None, modelos=None):
    """
    Para cada evento (vacía, llena), modelo y umbral de decisión: avisos, aciertos, precisión (de los
    avisos, cuántos ocurrieron), exhaustividad (de los que ocurrieron, cuántos se avisaron) y F1.
    'mejor' marca, por evento y modelo, el umbral con mayor F1.
    """
    umbrales = cfg.UMBRALES_DECISION if umbrales is None else umbrales
    modelos = MODELOS if modelos is None else modelos
    filas = []
    for ev, y in [("vacía", "y_vac"), ("llena", "y_lle")]:
        pref = "p_vac_" if ev == "vacía" else "p_lle_"
        for nombre, suf in modelos.items():
            col = pref + suf
            if col not in val:
                continue
            v = val.dropna(subset=[col, y])
            reales = int((v[y] == 1).sum())
            for u in umbrales:
                pred = v[col] > u
                vp = int((pred & (v[y] == 1)).sum())
                n_pred = int(pred.sum())
                prec = vp / n_pred if n_pred else np.nan
                exh = vp / reales if reales else np.nan
                f1 = 2 * prec * exh / (prec + exh) if (np.isfinite(prec) and np.isfinite(exh) and prec + exh > 0) else 0.0
                filas.append({"evento": ev, "modelo": nombre, "umbral": u, "avisos": n_pred, "aciertos": vp,
                              "casos_reales": reales, "precision": prec, "exhaustividad": exh, "F1": f1})
    t = pd.DataFrame(filas)
    if len(t):
        t["mejor"] = t.index.isin(t.groupby(["evento", "modelo"])["F1"].idxmax())
    return t


def texto_umbrales(t, modelo="Gemelo"):
    """Líneas de texto con la tabla del modelo pedido y el mejor umbral marcado con ★."""
    L = [f"Umbral de decisión ({modelo}): avisar si la probabilidad supera el umbral. "
         "F1 combina precisión y exhaustividad; ★ = mejor umbral."]
    for ev in ("vacía", "llena"):
        s = t[(t["modelo"] == modelo) & (t["evento"] == ev)]
        if s.empty:
            continue
        L.append(f"  Quedar {ev} ({int(s['casos_reales'].iloc[0])} casos reales):")
        for _, r in s.iterrows():
            L.append(f"   {'★' if r['mejor'] else ' '} umbral {r['umbral']:.1f}: {int(r['avisos']):>5} avisos · "
                     f"precisión {r['precision']:.3f} · exhaustividad {r['exhaustividad']:.3f} · F1 {r['F1']:.3f}")
    mejores = t[t["mejor"] & (t["modelo"] != modelo)]
    if len(mejores):
        L.append("  Mejor umbral de las referencias: " + "; ".join(
            f"{r['modelo']} {r['evento']} {r['umbral']:.1f} (F1 {r['F1']:.3f})" for _, r in mejores.iterrows()))
    return L


def figura_umbrales(t, modelo="Gemelo"):
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, ev in zip(axs, ("vacía", "llena")):
        s = t[(t["modelo"] == modelo) & (t["evento"] == ev)]
        if s.empty:
            continue
        ax.plot(s["umbral"], s["precision"], marker="o", color=NARANJA, label="Precisión")
        ax.plot(s["umbral"], s["exhaustividad"], marker="o", color=VERDE, label="Exhaustividad")
        ax.plot(s["umbral"], s["F1"], marker="o", color=AZUL, lw=2.4, label="F1")
        b = s[s["mejor"]].iloc[0]
        ax.axvline(b["umbral"], color=AZUL, lw=0.8, ls=":")
        ax.annotate(f"mejor: {b['umbral']:.1f}\nF1 {b['F1']:.2f}", (b["umbral"], b["F1"]), xytext=(6, 8),
                    textcoords="offset points", fontsize=8, color=AZUL, fontweight="bold")
        ax.set_title(f"Quedar {ev}", loc="left")
        ax.set_xlabel("Umbral de decisión (avisar si p > umbral)")
        ax.set_xticks(s["umbral"])
        estilo(ax)
    axs[0].set_ylabel(modelo)
    axs[0].legend(frameon=False, fontsize=8)
    fig.tight_layout()
    return fig


def bootstrap_dif(df, col_a, col_b, ycol, n=cfg.N_BOOTSTRAP, seed=cfg.SEMILLA):
    """IC 95 % de Brier(a) − Brier(b) remuestreando bloques día-estación."""
    d = df.assign(dif=(df[col_a] - df[ycol]) ** 2 - (df[col_b] - df[ycol]) ** 2)
    g = d.groupby(["fecha", "code"])["dif"].agg(["sum", "count"])
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(g), size=(n, len(g)))
    s, c = g["sum"].values, g["count"].values
    medias = s[idx].sum(1) / c[idx].sum(1)
    return d["dif"].mean(), np.percentile(medias, 2.5), np.percentile(medias, 97.5)


def informe(df, dp, c):
    import matplotlib.pyplot as plt
    val = df[df["ok"] & ~df["camion"]].copy()
    cam = df[df["ok"] & df["camion"]].copy()
    filas = []
    for ev, y in [("vacía", "y_vac"), ("llena", "y_lle")]:
        pref = "p_vac_" if ev == "vacía" else "p_lle_"
        base_p = (val[pref + "persist"] - val[y]) ** 2
        for nombre, suf in MODELOS.items():
            col = pref + suf
            v = val.dropna(subset=[col])
            b = ((v[col] - v[y]) ** 2).mean()
            fila = {"evento": ev, "modelo": nombre, "brier": b, "n": len(v),
                    "brier_con_camion": ((cam[col] - cam[y]) ** 2).mean() if len(cam) else np.nan,
                    "BSS_vs_persistencia": 1 - b / base_p.mean() if base_p.mean() > 0 else np.nan}
            if nombre != "Gemelo":
                v2 = val.dropna(subset=[col, pref + "gemelo"])
                dm, lo, hi = bootstrap_dif(v2, pref + "gemelo", col, y)
                fila.update(dif_gemelo_menos_este=dm, ic95_inf=lo, ic95_sup=hi)
            filas.append(fila)
    met = pd.DataFrame(filas)

    # B(t0+60): error absoluto y cobertura
    v = val.dropna(subset=["B60", "q50"])
    b60 = pd.DataFrame([
        {"modelo": "Gemelo", "MAE_mediana": (v["q50"] - v["B60"]).abs().mean(),
         "cobertura_IC80": ((v["B60"] >= v["q10"]) & (v["B60"] <= v["q90"])).mean(),
         "cobertura_IC90": ((v["B60"] >= v["q05"]) & (v["B60"] <= v["q95"])).mean()},
        {"modelo": "Sin resincronizar", "MAE_mediana": (v["sr_q50"] - v["B60"]).abs().mean(),
         "cobertura_IC80": ((v["B60"] >= v["sr_q10"]) & (v["B60"] <= v["sr_q90"])).mean(),
         "cobertura_IC90": np.nan},
        {"modelo": "Persistencia", "MAE_mediana": (v["B0"] - v["B60"]).abs().mean(),
         "cobertura_IC80": np.nan, "cobertura_IC90": np.nan}])

    # Precisión y exhaustividad con p > 0,5
    pr = []
    for ev, y in [("vacía", "y_vac"), ("llena", "y_lle")]:
        pref = "p_vac_" if ev == "vacía" else "p_lle_"
        for nombre, suf in MODELOS.items():
            pred = val[pref + suf] > 0.5
            vp = (pred & (val[y] == 1)).sum()
            pr.append({"evento": ev, "modelo": nombre, "precision": vp / max(pred.sum(), 1),
                       "exhaustividad": vp / max((val[y] == 1).sum(), 1), "frecuencia_real": val[y].mean()})
    pr = pd.DataFrame(pr)
    umb = tabla_umbrales(val)
    umb.round(4).to_csv(os.path.join(c, "umbrales_decision.csv"), index=False)
    fig = figura_umbrales(umb)
    fig.savefig(os.path.join(c, "umbrales_decision.png"), dpi=130)
    plt.close(fig)

    met.round(4).to_csv(os.path.join(c, "metricas_brier.csv"), index=False)
    b60.round(4).to_csv(os.path.join(c, "metricas_B60.csv"), index=False)
    pr.round(4).to_csv(os.path.join(c, "precision_exhaustividad.csv"), index=False)

    # Figura: Brier por hora del día
    fig, axs = plt.subplots(1, 2, figsize=(13, 4.5), sharey=True)
    colores = {"Gemelo": AZUL, "Sin resincronizar": NARANJA, "Persistencia": GRIS, "Persistencia 0/1": "0.75"}
    for ax, (ev, y) in zip(axs, [("vacía", "y_vac"), ("llena", "y_lle")]):
        pref = "p_vac_" if ev == "vacía" else "p_lle_"
        for nombre, suf in MODELOS.items():
            g = val.assign(e=(val[pref + suf] - val[y]) ** 2).groupby(val["hora"].astype(int))["e"].mean()
            ax.plot(g.index, g.values, marker="o", ms=3, color=colores[nombre], label=nombre,
                    lw=2 if nombre == "Gemelo" else 1.2)
        ax.set_title(f"Quedar {ev}", loc="left")
        ax.set_xlabel("Hora del pronóstico")
        estilo(ax)
    axs[0].set_ylabel("Puntaje de Brier (menor es mejor)")
    axs[0].legend(frameon=False, fontsize=8)
    fig.suptitle("Puntaje de Brier por hora del día — semana de evaluación", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(os.path.join(c, "brier_por_hora.png"), dpi=130)

    # Figura: calibración
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.8))
    cortes = np.linspace(0, 1, 11)
    calib = []
    for ax, (ev, y) in zip(axs, [("vacía", "y_vac"), ("llena", "y_lle")]):
        pref = "p_vac_" if ev == "vacía" else "p_lle_"
        ax.plot([0, 1], [0, 1], color="k", lw=0.8)
        for nombre, suf in [("Gemelo", "gemelo"), ("Sin resincronizar", "sin_resinc")]:
            s = val.dropna(subset=[pref + suf])
            tramo = pd.cut(s[pref + suf], cortes, include_lowest=True)
            g = s.groupby(tramo, observed=True).agg(p=(pref + suf, "mean"), f=(y, "mean"), n=(y, "size"))
            ax.plot(g["p"], g["f"], marker="o", color=colores[nombre], label=nombre)
            for _, r in g.iterrows():
                if nombre == "Gemelo":
                    ax.annotate(f"{int(r['n'])}", (r["p"], r["f"]), fontsize=6.5, xytext=(3, -8),
                                textcoords="offset points", color=AZUL)
            g2 = g.copy()
            g2.index = g2.index.astype(str)
            calib.append(g2.rename_axis("tramo").reset_index().assign(evento=ev, modelo=nombre))
        ax.set_xlabel("Probabilidad pronosticada")
        ax.set_ylabel("Fracción que realmente ocurrió")
        ax.set_title(f"Calibración: quedar {ev}", loc="left")
        estilo(ax)
    axs[0].legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(c, "calibracion.png"), dpi=130)
    pd.concat(calib, ignore_index=True).round(4).to_csv(os.path.join(c, "calibracion.csv"), index=False)

    L = [f"Evaluación: {val['t0'].min():%d/%m} a {val['t0'].max():%d/%m}, {val['t0'].nunique()} instantes, "
         f"{len(val)} pares estación-hora válidos ({len(cam)} con camión del operador, aparte)", "",
         "Puntaje de Brier (menor es mejor):"]
    for _, r in met.iterrows():
        t = f"  {r['evento']:<6} {r['modelo']:<18} {r['brier']:.4f}   BSS vs persistencia {r['BSS_vs_persistencia']:+.3f}"
        if np.isfinite(r.get("dif_gemelo_menos_este", np.nan)):
            t += f"   gemelo − este {r['dif_gemelo_menos_este']:+.4f} (IC95 {r['ic95_inf']:+.4f} a {r['ic95_sup']:+.4f})"
        L.append(t)
    L += ["", "B(t0+60):", b60.round(3).to_string(index=False), "", "Con p > 0,5:", pr.round(3).to_string(index=False)]
    L += [""] + texto_umbrales(umb)

    if dp is not None and len(dp):
        resumen = []
        for nombre, g in dp.groupby("plan", sort=False):
            x = g["atendidos_extra_vs_sin_accion"].values
            se = x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else np.nan
            resumen.append({"plan": nombre, "horas": len(x), "atendidos_extra_media": x.mean(),
                            "ic95_inf": x.mean() - 1.96 * se, "ic95_sup": x.mean() + 1.96 * se,
                            "no_atendida_media": g["no_atendida_media"].mean(),
                            "bicis_movidas_media": g["bicis_movidas"].mean()})
        resumen = pd.DataFrame(resumen)
        resumen.round(3).to_csv(os.path.join(c, "planes_resumen.csv"), index=False)
        L += ["", "Valor de los planes (sólo en simulación; usuarios atendidos de más por hora vs sin acción):",
              resumen.round(2).to_string(index=False)]
        fig, ax = plt.subplots(figsize=(10, 4.5))
        dp2 = dp.assign(h=pd.to_datetime(dp["t0"]).dt.hour)
        for nombre, color in [("Regla umbral", GRIS), ("Gemelo (voraz)", VERDE),
                              ("Gemelo (voraz) con tiempos de viaje", "#7fbf9f")]:
            g = dp2[dp2["plan"] == nombre].groupby("h")["atendidos_extra_vs_sin_accion"].mean()
            if len(g):
                ax.plot(g.index, g.values, marker="o", color=color, label=nombre)
        ax.axhline(0, color="k", lw=0.8)
        ax.set_xlabel("Hora")
        ax.set_ylabel("Usuarios atendidos de más por hora")
        ax.set_title("Valor de los planes de rebalanceo por hora (en simulación)", loc="left")
        ax.legend(frameon=False, fontsize=8)
        estilo(ax)
        fig.tight_layout()
        fig.savefig(os.path.join(c, "planes_por_hora.png"), dpi=130)
    texto = "\n".join(L) + "\n"
    with open(os.path.join(c, "resumen_evaluacion.txt"), "w", encoding="utf-8") as fh:
        fh.write(texto)
    plt.close("all")
    print(texto)
    print(f"Resultados en {c}")
    return met


# =====================================================================
# Gemelo en vivo: un ciclo completo (lo corre GitHub Actions cada 15 min)
# =====================================================================
ARCH_PRON = "pronosticos.csv"
ARCH_EVAL = "evaluaciones.csv"


def ahora_local():
    try:
        return pd.Timestamp.now(tz=cfg.ZONA).tz_localize(None)
    except Exception:
        return pd.Timestamp.now(tz="UTC").tz_localize(None) - pd.Timedelta(hours=6)


def ciclo_en_vivo(gem, t0=None, R=None):
    """
    1) lee el estado real, 2) pronostica la próxima hora y arma el plan, 3) guarda el pronóstico
    en gemelo_vivo/pronosticos.csv, 4) evalúa contra lo ocurrido los pronósticos de hace más de
    una hora, 5) reescribe gemelo_vivo/README.md (GitHub lo muestra como página).
    t0 = None: en vivo. Con t0 se repite un ciclo pasado (sirve para probar).
    """
    cv = cfg.CARPETA_VIVO if t0 is None else cfg.CARPETA_VIVO + "_prueba"   # las pruebas no ensucian el registro
    os.makedirs(cv, exist_ok=True)
    if t0 is None:
        t0, estado = gem.estado_vivo()
        modo = "en vivo"
    else:
        t0 = pd.Timestamp(t0)
        estado = gem.estado(t0)
        modo = "reproducción"
    t0 = pd.Timestamp(t0).floor("min")
    archivo = os.path.join(cv, ARCH_PRON)
    previos = pd.read_csv(archivo, usecols=["t0"], parse_dates=["t0"]) if os.path.isfile(archivo) else None
    ya = previos is not None and (previos["t0"] == t0).any()

    if not (cfg.HORA_INICIO_VIVO <= f"{t0:%H:%M}" <= cfg.HORA_FIN_VIVO):
        print(f"{t0:%d/%m %H:%M}: fuera del horario {cfg.HORA_INICIO_VIVO}-{cfg.HORA_FIN_VIVO}; "
              "sólo se evalúan pronósticos pendientes")
    elif ya:
        print(f"{t0:%d/%m %H:%M}: ya hay un pronóstico para este minuto")
    else:
        res = simulacion_una_hora(gem, t0, en_vivo=(modo == "en vivo"), R=R, con_referencias=False,
                                  estado=estado, carpeta_salida=os.path.join(cv, "ultimo"))
        e, p = res["pron"]["estado"], res["pron"]
        nan = np.full(gem.I, np.nan)
        ps = {"p_vac": nan, "p_lle": nan}
        try:
            if t0.hour >= 6:
                ps = gem.pron_sin_resinc(gem.sin_resincronizar_dia(t0.normalize(), R=R), t0)
        except Exception as ex:
            print(f"Aviso: sin la referencia 'sin resincronizar' en este ciclo ({ex})")
        pv, pl, v01, l01 = p_persistencia(leer_persistencia(), e["B0"], e["C"] - e["B0"])
        filas = pd.DataFrame({
            "t0": t0, "modo": modo, "habil": bool(es_habil([t0])[0]), "code": gem.est["code"],
            "ok": e["ok"], "B0": e["B0"], "C": e["C"],
            "p_vac_gemelo": p["p_vac"], "p_lle_gemelo": p["p_lle"],
            "q10": p["q10"], "q50": p["q50"], "q90": p["q90"],
            "p_vac_sin_resinc": ps["p_vac"], "p_lle_sin_resinc": ps["p_lle"],
            "p_vac_persist": pv, "p_lle_persist": pl, "p_vac_persist01": v01, "p_lle_persist01": l01,
            "cambio_plan_gemelo": res["tabla"]["cambio_plan_gemelo"],
            "W": gem.params["W"], "m": gem.params["m"], "phi": p["phi"],
            "F_ret": p["info"]["F"]["ret"], "F_dev": p["info"]["F"]["dev"]})
        filas.round(4).to_csv(archivo, mode="a", header=not os.path.isfile(archivo), index=False)
        print(res["texto"])
    resumen = evaluar_pendientes(gem, cv)
    escribir_pagina(resumen, cv)
    print(f"Registro en {cv}/")
    return resumen


def evaluar_pendientes(gem, cv=cfg.CARPETA_VIVO):
    """Compara con lo ocurrido los pronósticos cuya hora ya terminó y resume el puntaje en vivo."""
    import matplotlib.pyplot as plt
    a_pron, a_eval = os.path.join(cv, ARCH_PRON), os.path.join(cv, ARCH_EVAL)
    if not os.path.isfile(a_pron):
        return None
    pron = pd.read_csv(a_pron, parse_dates=["t0"], dtype={"code": str})
    ev = pd.read_csv(a_eval, parse_dates=["t0"], dtype={"code": str}) if os.path.isfile(a_eval) else None
    hechos = set(ev["t0"]) if ev is not None else set()
    ultima = gem.panel.ultima_lectura()
    pend = sorted(t for t in set(pron["t0"]) - hechos
                  if ultima is not None and t + pd.Timedelta(minutes=61) <= ultima and t >= gem.panel.t_ini)
    nuevas = []
    for t in pend:
        o = gem.observado(t)
        if o is None:
            continue
        nuevas.append(pd.DataFrame({"t0": t, "code": gem.est["code"], "y_vac": o["y_vac"].astype(int),
                                    "y_lle": o["y_lle"].astype(int), "B60": o["B60"], "camion": o["camion"],
                                    "ok_obs": o["ok"]}))
    if nuevas:
        nuevas = pd.concat(nuevas, ignore_index=True)
        nuevas.to_csv(a_eval, mode="a", header=not os.path.isfile(a_eval), index=False)
        ev = pd.read_csv(a_eval, parse_dates=["t0"], dtype={"code": str})
        print(f"Evaluados {len(pend)} pronósticos de hace más de una hora")
    if ev is None or ev.empty:
        return {"df": None, "tabla": None, "n": 0, "pron": pron}

    df = pron.merge(ev, on=["t0", "code"])
    val = df[df["ok"].astype(bool) & df["ok_obs"].astype(bool) & ~df["camion"].astype(bool)]
    filas = []
    for grupo, sub in [("días hábiles", val[val["habil"].astype(bool)]), ("todos los días", val)]:
        for nombre, suf in MODELOS.items():
            fila = {"dias": grupo, "modelo": nombre, "instantes": sub["t0"].nunique(), "pares": len(sub)}
            for ev_, y in [("vacia", "y_vac"), ("llena", "y_lle")]:
                col = ("p_vac_" if ev_ == "vacia" else "p_lle_") + suf
                s = sub.dropna(subset=[col])
                fila[f"brier_{ev_}"] = ((s[col] - s[y]) ** 2).mean() if len(s) else np.nan
            filas.append(fila)
    tabla = pd.DataFrame(filas)
    tabla.round(4).to_csv(os.path.join(cv, "resumen_vivo.csv"), index=False)

    if len(val):
        fig, ax = plt.subplots(figsize=(9, 4))
        colores = {"Gemelo": AZUL, "Sin resincronizar": NARANJA, "Persistencia": GRIS}
        dia = val["t0"].dt.normalize()
        for nombre, suf in MODELOS.items():
            if nombre not in colores:
                continue
            e2 = (((val["p_vac_" + suf] - val["y_vac"]) ** 2 + (val["p_lle_" + suf] - val["y_lle"]) ** 2) / 2)
            g = e2.groupby(dia).mean()
            ax.plot(g.index, g.values, marker="o", color=colores[nombre], label=nombre,
                    lw=2 if nombre == "Gemelo" else 1.2)
        ax.set_ylabel("Brier (promedio vacía y llena)")
        ax.set_title("Puntaje de Brier de los pronósticos hechos en tiempo real, por día", loc="left")
        ax.legend(frameon=False, fontsize=8)
        estilo(ax)
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(os.path.join(cv, "brier_vivo.png"), dpi=110)
        plt.close(fig)
    return {"df": df, "tabla": tabla, "n": val["t0"].nunique(), "pron": pron}


def escribir_pagina(resumen, cv=cfg.CARPETA_VIVO):
    """gemelo_vivo/README.md: GitHub lo muestra al abrir la carpeta, con el mapa y el puntaje."""
    L = ["# Gemelo digital Ecobici · en vivo", "",
         f"Página actualizada automáticamente el {ahora_local():%d/%m/%Y %H:%M} (hora de Ciudad de México).", ""]
    ult = os.path.join(cv, "ultimo")
    if resumen is not None and resumen.get("pron") is not None and len(resumen["pron"]):
        t0 = resumen["pron"]["t0"].max()
        L += [f"## Último pronóstico: {t0:%d/%m %H:%M} a {t0 + pd.Timedelta(minutes=60):%H:%M}", "",
              "![Mapa](ultimo/mapa.png)", ""]
        a = os.path.join(ult, "clima.csv")
        if os.path.isfile(a):
            cl = pd.read_csv(a)
            tot = cl[cl["variable"] == "efecto total en la hora"].iloc[-1]
            fuente = tot["fuente"] if "fuente" in cl and isinstance(tot["fuente"], str) else ""
            L += [f"### Clima {fuente} de la hora y su efecto en la demanda".replace("  ", " "), ""]
            if fuente == "pronosticado":
                L += ["_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._", ""]
            if np.isfinite(tot["temperatura_c"]):
                ll = tot["precipitacion_mm"]
                L.append(f"**{tot['temperatura_c']:.1f} °C** · "
                         + ("sin lluvia" if not np.isfinite(ll) or ll < cfg.UMBRAL_LLUVIA else f"lluvia {ll:.1f} mm/h")
                         + f" · viento {tot['viento_kmh']:.0f} km/h · día {tot['tipo_dia']}")
            else:
                L.append("Sin datos de clima para esta hora: se toma como normal.")
            L += ["", f"El clima multiplica los **retiros por {tot['factor_retiros']:.2f}** y las "
                  f"**devoluciones por {tot['factor_devoluciones']:.2f}** (1,00 = sin efecto).", ""]
            det = cl[cl["variable"] != "efecto total en la hora"]
            if len(det):
                L += ["| Variable | Condición | Factor retiros | Factor devoluciones |", "| --- | --- | --- | --- |"]
                for _, r in det.iterrows():
                    L.append(f"| {r['variable']} | {r['categoria']} | {r['factor_retiros']:.3f} | "
                             f"{r['factor_devoluciones']:.3f} |")
                L.append("")
        a = os.path.join(ult, "pronostico_estaciones.csv")
        if os.path.isfile(a):
            t = pd.read_csv(a, dtype={"code": str})
            t["riesgo"] = np.fmax(t["p_vacia"], t["p_llena"])
            t = t.sort_values("riesgo", ascending=False).head(10)
            L += ["| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |",
                  "| --- | --- | --- | --- | --- |"]
            for _, r in t.iterrows():
                L.append(f"| {r['code']} {str(r['nombre'])[:28]} | {r['B_t0']:.0f} / {r['C']:.0f} | "
                         f"{r['p_vacia']:.2f} | {r['p_llena']:.2f} | {r['B_t60_ic80']} |")
            L.append("")
        a = os.path.join(ult, "plan_traslados.csv")
        if os.path.isfile(a) and os.path.getsize(a) > 5:
            try:
                tr = pd.read_csv(a, dtype={"origen": str, "destino": str})
            except pd.errors.EmptyDataError:
                tr = pd.DataFrame()
            g = tr[tr["plan"] == "Gemelo (voraz)"] if len(tr) else tr
            L += ["### Plan recomendado del camión", ""]
            if len(g):
                for _, r in g.iterrows():
                    L.append(f"{r['orden']}. Llevar **{r['bicis']} bicis** de {r['origen']} "
                             f"({r['B_origen']}/{r['C_origen']}) a {r['destino']} ({r['B_destino']}/{r['C_destino']})")
            else:
                L.append("Ningún traslado mejora la hora lo suficiente.")
            L.append("")
    if resumen is not None and resumen.get("tabla") is not None:
        tb = resumen["tabla"]
        tb = tb[tb["dias"] == "días hábiles"] if (tb["dias"] == "días hábiles").any() else tb
        L += ["## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)", "",
              f"{resumen['n']} pronósticos evaluados contra lo que ocurrió una hora después "
              "(sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.", "",
              "| Modelo | Brier vacía | Brier llena |", "| --- | --- | --- |"]
        for _, r in tb.iterrows():
            L.append(f"| {r['modelo']} | {r['brier_vacia']:.3f} | {r['brier_llena']:.3f} |")
        L += ["", "![Brier por día](brier_vivo.png)", ""]
    L += ["## Detalle", "", "![Abanico](ultimo/abanico.png)", "",
          "Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), "
          "`resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo)."]
    with open(os.path.join(cv, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# =====================================================================
# Programa principal
# =====================================================================
def main():
    matplotlib.use("Agg")
    ap = argparse.ArgumentParser(description="Gemelo digital Ecobici (30 estaciones)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("preparar", help="lee y revisa todos los datos")
    h = sub.add_parser("hora", help="simulación de una hora")
    h.add_argument("t0", nargs="?", help='instante, ej. "2026-11-26 07:45"')
    h.add_argument("--en-vivo", action="store_true")
    for nombre in ("validar", "ajuste", "evaluar"):
        p = sub.add_parser(nombre)
        p.add_argument("--desde", required=True)
        p.add_argument("--hasta", required=True)
        if nombre == "evaluar":
            p.add_argument("--planes", action="store_true", help="evalúa también los planes (más lento)")
        if nombre == "validar":
            p.add_argument("--horas", type=int, default=40)
    tz = sub.add_parser("tasas", help="cómo cambian las tasas en el día y entre días, frente a lo observado")
    tz.add_argument("--desde", required=True)
    tz.add_argument("--hasta", required=True)
    tz.add_argument("--estacion", default=None, help="código de una estación (por defecto, las 30 sumadas)")
    tz.add_argument("--horas", default="08:00,13:00,18:00", help="horas para comparar entre días, separadas por coma")
    c = sub.add_parser("ciclo", help="un ciclo del gemelo en vivo: pronostica, registra y evalúa")
    c.add_argument("--t0", default=None, help="repetir un ciclo pasado (para probar)")
    for p in sub.choices.values():
        p.add_argument("--R", type=int, default=None, help="réplicas")
    a = ap.parse_args()
    os.makedirs(cfg.CARPETA_RESULTADOS, exist_ok=True)

    if a.cmd == "hora" and not a.t0 and not a.en_vivo:
        ap.error('indica el instante, por ejemplo: hora "2026-11-26 07:45", o usa --en-vivo')
    if a.cmd == "ciclo":
        ref = pd.Timestamp(a.t0) if a.t0 else ahora_local()
        gem = Gemelo(en_vivo=a.t0 is None, feed_desde=ref - pd.Timedelta(days=cfg.FEED_DIAS_VIVO))
        ciclo_en_vivo(gem, a.t0, a.R)
        return
    gem = Gemelo(en_vivo=getattr(a, "en_vivo", False))
    if a.cmd == "preparar":
        c = carpeta()
        gem.tabla_base.round(4).to_csv(os.path.join(c, "perfil_base_15min.csv"), index=False)
        gem.tabla_base.round(4).to_csv(cfg.ARCHIVO_PERFIL_BASE, index=False)
        print(f"Perfil base guardado en {os.path.join(c, 'perfil_base_15min.csv')} y en {cfg.ARCHIVO_PERFIL_BASE} "
              "(este último es el que usa el gemelo en GitHub, sin los viajes)")
        print(f"Última lectura del feed: {gem.panel.ultima_lectura()}")
    elif a.cmd == "hora":
        res = simulacion_una_hora(gem, a.t0, en_vivo=a.en_vivo, R=a.R)
        print(res["texto"])
        print(f"Resultados en {res['carpeta']}")
    elif a.cmd == "validar":
        validar(gem, a.desde, a.hasta, a.horas, a.R)
    elif a.cmd == "ajuste":
        ajuste(gem, a.desde, a.hasta, a.R)
    elif a.cmd == "evaluar":
        evaluar(gem, a.desde, a.hasta, a.planes, a.R)
    elif a.cmd == "tasas":
        from tasas_gemelo import comando_tasas
        comando_tasas(gem, a.desde, a.hasta, [h.strip() for h in a.horas.split(",") if h.strip()], a.estacion)


if __name__ == "__main__":
    main()
