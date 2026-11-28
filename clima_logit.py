"""
clima_logit.py - Efecto del clima con regresión logística

Variable a explicar (una fila por estación y pronóstico, cada 15 min de 06:00 a 22:45, días hábiles):
    y = 1 si la estación quedó VACÍA en algún minuto de la hora siguiente (otro modelo para LLENA).

Dos modelos por evento:
  1. ¿El clima afecta?        y ~ clima + ocupación inicial + franja horaria + perfil de la estación
  2. ¿El gemelo ya lo capta?  y ~ clima + logit(probabilidad que dio el gemelo)
     Si en el modelo 2 los betas del clima son ~0, el gemelo ya incorpora el efecto del clima.

Variables de clima (de la misma tabla por hora que usa el gemelo, hora que cubre la mayor parte del pronóstico):
    llueve          1 si llueve en la hora (>= UMBRAL_LLUVIA mm)
    lluvia_previa   1 si llovió en las 3 h previas (>= UMBRAL_LLUVIA_PREVIA mm)
    temp_dif_c      temperatura respecto de lo normal para ese mes y hora (°C)
    viento_5kmh     viento en unidades de 5 km/h

Errores estándar robustos por conglomerado (día-hora): el clima es el mismo para las 30 estaciones en una
misma hora, así que tratar cada fila como independiente daría intervalos demasiado estrechos.

Los betas se leen en escala logit; exp(beta) es la razón de odds (OR): OR = 0,8 -> 20 % menos chance (en odds).

Uso:  py -3.14 gemelo.py clima_logit --desde 2026-11-09 --hasta 2026-11-20
      (opcional) --validar-desde 2026-11-23 --validar-hasta 2026-11-27
"""
import os

import numpy as np
import pandas as pd
from scipy import stats

import config_gemelo as cfg

VARS_CLIMA = ["llueve", "lluvia_previa", "temp_dif_c", "viento_5kmh"]
NOMBRES = {"llueve": "Llueve en la hora", "lluvia_previa": "Llovió en las 3 h previas",
           "temp_dif_c": "Temperatura vs normal (+1 °C)", "viento_5kmh": "Viento (+5 km/h)"}
FRANJAS = [(6, 7), (7, 10), (10, 17), (17, 20), (20, 24)]


# ---------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------
def _clima_t0(gem, t0):
    h = (pd.Timestamp(t0) + pd.Timedelta(minutes=30)).floor("h")
    c = gem.clima
    if c is None or h not in c.index:
        return None
    r = c.loc[h]
    if not (np.isfinite(r["precipitacion_mm"]) and np.isfinite(r["temp_dif_c"]) and np.isfinite(r["viento_kmh"])):
        return None
    previa = r["lluvia_previa_mm"] if np.isfinite(r["lluvia_previa_mm"]) else 0.0
    return {"llueve": float(r["precipitacion_mm"] >= cfg.UMBRAL_LLUVIA),
            "lluvia_previa": float(previa >= cfg.UMBRAL_LLUVIA_PREVIA),
            "temp_dif_c": float(r["temp_dif_c"]), "viento_5kmh": float(r["viento_kmh"]) / 5,
            "precipitacion_mm": float(r["precipitacion_mm"]), "temperatura_c": float(r["temperatura_c"])}


def armar_datos(gem, desde, hasta, R=None):
    """Una fila por estación válida y pronóstico: lo observado, el estado inicial, el clima y la p del gemelo."""
    from gemelo import lista_t0
    R = cfg.R_AJUSTE if R is None else R
    t0s = lista_t0(gem, desde, hasta)
    filas, sin_clima = [], 0
    for k, t0 in enumerate(t0s):
        if k % 68 == 0:
            print(f"  {t0:%d/%m} ({k + 1} de {len(t0s)} pronósticos)")
        cl = _clima_t0(gem, t0)
        if cl is None:
            sin_clima += 1
            continue
        o = gem.observado(t0)
        if o is None:
            continue
        p = gem.pronosticar(t0, R=R)
        e = p["estado"]
        val = e["ok"] & o["ok"] & ~o["camion"]
        if not val.any():
            continue
        filas.append(pd.DataFrame({
            "t0": t0, "code": gem.est["code"].values[val], "perfil": gem.est["perfil"].values[val],
            "B0": e["B0"][val], "C": e["C"][val], "hora": t0.hour + t0.minute / 60,
            "y_vac": o["y_vac"][val].astype(int), "y_lle": o["y_lle"][val].astype(int),
            "p_vac_gemelo": p["p_vac"][val], "p_lle_gemelo": p["p_lle"][val], **cl}))
    if sin_clima:
        print(f"Aviso: {sin_clima} pronósticos sin clima se omitieron (¿falta datos/clima/clima_horario.csv?)")
    if not filas:
        raise SystemExit("No hay datos con clima en ese periodo")
    return pd.concat(filas, ignore_index=True)


def _grupo_bicis(b):
    """Grupos 0, 1, 2, 3-4, 5-7, 8+ (los de CORTES_PERSISTENCIA), en orden."""
    cortes = [0] + list(cfg.CORTES_PERSISTENCIA) + [np.inf]
    etiquetas = ["0"] + [f"{a}" if b_ - a == 1 else (f"{a}-{int(b_) - 1}" if np.isfinite(b_) else f"{a}+")
                         for a, b_ in zip(cortes[1:-1], cortes[2:])]
    g = pd.cut(b, [-0.5] + [c - 0.5 for c in cortes[1:-1]] + [np.inf], labels=etiquetas)
    return g.astype(str), etiquetas


def matriz(df, evento, modelo):
    """Matriz de diseño. modelo 1: clima + controles; modelo 2: clima + logit(p del gemelo)."""
    X = pd.DataFrame({"constante": 1.0}, index=df.index)
    for v in VARS_CLIMA:
        X[v] = df[v]
    if modelo == 1:
        # Ocupación inicial: bicis (para vacía) o anclajes libres (para llena), en grupos; base = el grupo más alto
        n = df["B0"] if evento == "vac" else df["C"] - df["B0"]
        g, etiquetas = _grupo_bicis(n)
        orden = [x for x in etiquetas if x in set(g)]
        for nivel in orden[:-1]:
            X[f"{'bicis' if evento == 'vac' else 'anclajes'}_{nivel}"] = (g == nivel).astype(float)
        f = pd.cut(df["hora"], [a for a, _ in FRANJAS] + [FRANJAS[-1][1]], right=False,
                   labels=[f"{a:02d}-{b:02d}h" for a, b in FRANJAS]).astype(str)
        for nivel in sorted(f.unique())[1:]:
            X[f"franja_{nivel}"] = (f == nivel).astype(float)
        for nivel in sorted(df["perfil"].astype(str).unique())[1:]:
            X[f"perfil_{nivel}"] = (df["perfil"].astype(str) == nivel).astype(float)
    else:
        p = df[f"p_{evento}_gemelo"].clip(1e-3, 1 - 1e-3)
        X["logit_p_gemelo"] = np.log(p / (1 - p))
    X = X.loc[:, X.std(ddof=0).gt(0) | (X.columns == "constante")]   # columnas constantes (p. ej. nunca llovió) fuera
    return X


# ---------------------------------------------------------------------
# Regresión logística (Newton-Raphson) con errores robustos por conglomerado
# ---------------------------------------------------------------------
def logit(X, y, grupos=None, max_iter=100, tol=1e-9, ridge=1e-8):
    Xv, yv = np.asarray(X, float), np.asarray(y, float)
    beta = np.zeros(Xv.shape[1])
    for _ in range(max_iter):
        p = 1 / (1 + np.exp(-np.clip(Xv @ beta, -30, 30)))
        W = p * (1 - p)
        H = Xv.T @ (Xv * W[:, None]) + ridge * np.eye(len(beta))
        paso = np.linalg.solve(H, Xv.T @ (yv - p))
        beta += paso
        if np.max(np.abs(paso)) < tol:
            break
    p = 1 / (1 + np.exp(-np.clip(Xv @ beta, -30, 30)))
    Hinv = np.linalg.inv(Xv.T @ (Xv * (p * (1 - p))[:, None]) + ridge * np.eye(len(beta)))
    if grupos is None:
        V = Hinv
    else:                                                   # sándwich por conglomerado (CR1)
        u = Xv * (yv - p)[:, None]
        S = pd.DataFrame(u).groupby(np.asarray(grupos)).sum().values
        G, n, k = S.shape[0], len(yv), Xv.shape[1]
        V = Hinv @ (S.T @ S) @ Hinv * (G / (G - 1)) * ((n - 1) / (n - k))
    ee = np.sqrt(np.diag(V))
    ll = float(np.sum(yv * np.log(np.clip(p, 1e-12, 1)) + (1 - yv) * np.log(np.clip(1 - p, 1e-12, 1))))
    return {"beta": beta, "ee": ee, "p": p, "loglik": ll, "columnas": list(X.columns)}


def tabla_coeficientes(fit, evento, modelo):
    b, ee = fit["beta"], fit["ee"]
    z = b / ee
    out = pd.DataFrame({"evento": "vacía" if evento == "vac" else "llena", "modelo": modelo,
                        "variable": fit["columnas"], "beta": b, "ee_robusto": ee, "z": z,
                        "p_valor": 2 * stats.norm.sf(np.abs(z)),
                        "OR": np.exp(b), "OR_ic95_inf": np.exp(b - 1.96 * ee), "OR_ic95_sup": np.exp(b + 1.96 * ee)})
    out["es_clima"] = out["variable"].isin(VARS_CLIMA)
    return out


def predecir(fit, X):
    Xv = np.asarray(X.reindex(columns=fit["columnas"], fill_value=0.0), float)
    return 1 / (1 + np.exp(-np.clip(Xv @ fit["beta"], -30, 30)))


# ---------------------------------------------------------------------
# Gráfico de efectos del clima
# ---------------------------------------------------------------------
def figura(coef):
    import matplotlib.pyplot as plt
    c = coef[coef["es_clima"]]
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.8), sharex=True)
    colores = {1: "#1f4e79", 2: "#d68910"}
    etiquetas = {1: "1 · ¿el clima afecta? (con controles)", 2: "2 · ¿el gemelo ya lo capta? (con p del gemelo)"}
    for ax, ev in zip(axs, ("vacía", "llena")):
        s = c[c["evento"] == ev]
        for m, dy in ((1, -0.12), (2, 0.12)):
            sm = s[s["modelo"] == m]
            y = [VARS_CLIMA.index(v) + dy for v in sm["variable"]]
            ax.errorbar(sm["OR"], y, xerr=[sm["OR"] - sm["OR_ic95_inf"], sm["OR_ic95_sup"] - sm["OR"]],
                        fmt="o", color=colores[m], ms=5, capsize=3, label=etiquetas[m])
        ax.axvline(1, color="#999999", lw=0.9)
        ax.set_yticks(range(len(VARS_CLIMA)), [NOMBRES[v] for v in VARS_CLIMA], fontsize=8)
        ax.invert_yaxis()
        ax.set_xscale("log")
        from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter
        marcas = [0.5, 0.75, 1, 1.5, 2]
        ax.xaxis.set_major_locator(FixedLocator(marcas))
        ax.xaxis.set_major_formatter(FixedFormatter(["0,5", "0,75", "1", "1,5", "2"]))
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.set_title(f"Quedar {ev}", loc="left")
        ax.set_xlabel("Razón de odds (IC95, escala log) · 1 = sin efecto")
        ax.spines[["top", "right"]].set_visible(False)
    axs[0].legend(frameon=False, fontsize=7.5, loc="lower left", bbox_to_anchor=(0, 1.08))
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------
# Comando
# ---------------------------------------------------------------------
def comando(gem, desde, hasta, validar_desde=None, validar_hasta=None, R=None):
    import matplotlib.pyplot as plt
    c = os.path.join(cfg.CARPETA_RESULTADOS, "clima_logit")
    os.makedirs(c, exist_ok=True)
    print(f"Regresión logística del clima · entrenamiento {desde} a {hasta}")
    df = armar_datos(gem, desde, hasta, R)
    df.to_csv(os.path.join(c, "datos_entrenamiento.csv"), index=False)
    grupos = pd.to_datetime(df["t0"]).dt.floor("h")
    n_h = grupos.nunique()
    h_lluvia = df.groupby(grupos)["llueve"].first().sum()

    coefs, fits = [], {}
    for ev in ("vac", "lle"):
        for m in (1, 2):
            X = matriz(df, ev, m)
            fit = logit(X, df[f"y_{ev}"], grupos)
            fits[(ev, m)] = (fit, X.columns)
            coefs.append(tabla_coeficientes(fit, ev, m))
    coef = pd.concat(coefs, ignore_index=True)
    coef.round(5).to_csv(os.path.join(c, "coeficientes.csv"), index=False)
    fig = figura(coef)
    fig.savefig(os.path.join(c, "efectos_clima.png"), dpi=130)
    plt.close(fig)

    L = [f"Regresión logística del clima · entrenamiento {pd.Timestamp(desde):%d/%m} a {pd.Timestamp(hasta):%d/%m}",
         f"{len(df)} filas estación-pronóstico · {df['t0'].nunique()} pronósticos · {n_h} horas "
         f"({int(h_lluvia)} con lluvia) · errores robustos por conglomerado día-hora", "",
         "Beta en escala logit; OR = exp(beta) = cuánto se multiplican las odds. * p < 0,05", ""]
    for ev, nombre in (("vac", "vacía"), ("lle", "llena")):
        L.append(f"Quedar {nombre} ({int(df[f'y_{ev}'].sum())} de {len(df)} casos, "
                 f"{100 * df[f'y_{ev}'].mean():.1f} %)")
        for m, titulo in ((1, "Modelo 1 · ¿el clima afecta? (con ocupación, franja y perfil)"),
                          (2, "Modelo 2 · ¿el gemelo ya lo capta? (con logit de la p del gemelo)")):
            L.append(f"  {titulo}")
            s = coef[(coef["evento"] == nombre) & (coef["modelo"] == m) & coef["es_clima"]]
            for _, r in s.iterrows():
                L.append(f"    {NOMBRES[r['variable']]:<30} beta {r['beta']:+.3f} (ee {r['ee_robusto']:.3f})  "
                         f"OR {r['OR']:.2f} [{r['OR_ic95_inf']:.2f}–{r['OR_ic95_sup']:.2f}]  "
                         f"p = {r['p_valor']:.3f}{' *' if r['p_valor'] < 0.05 else ''}")
            faltan = [NOMBRES[v] for v in VARS_CLIMA if v not in set(s["variable"])]
            if faltan:
                L.append(f"    (sin variación en el periodo, no se estima: {', '.join(faltan)})")
        L.append("")

    if validar_desde and validar_hasta:
        print(f"Validación {validar_desde} a {validar_hasta}")
        dv = armar_datos(gem, validar_desde, validar_hasta, R)
        dv.to_csv(os.path.join(c, "datos_validacion.csv"), index=False)
        L.append(f"Validación {pd.Timestamp(validar_desde):%d/%m} a {pd.Timestamp(validar_hasta):%d/%m} "
                 f"({len(dv)} filas) · Brier (menor es mejor):")
        for ev, nombre in (("vac", "vacía"), ("lle", "llena")):
            y = dv[f"y_{ev}"].values
            b_gem = np.mean((dv[f"p_{ev}_gemelo"] - y) ** 2)
            # recalibración sin clima vs con clima, ambas ajustadas en entrenamiento
            X2 = matriz(df, ev, 2)
            sin = [col for col in X2.columns if col not in VARS_CLIMA]
            fit_sin = logit(X2[sin], df[f"y_{ev}"])
            Xv = matriz(dv, ev, 2)
            b_sin = np.mean((predecir(fit_sin, Xv) - y) ** 2)
            b_con = np.mean((predecir(fits[(ev, 2)][0], Xv) - y) ** 2)
            L.append(f"  {nombre:<6} gemelo {b_gem:.4f} · gemelo recalibrado sin clima {b_sin:.4f} · "
                     f"gemelo + clima {b_con:.4f}")
        L.append("")

    texto = "\n".join(L) + "\n"
    with open(os.path.join(c, "resumen.txt"), "w", encoding="utf-8") as fh:
        fh.write(texto)
    print(texto)
    print(f"Resultados en {c}")
    return coef
