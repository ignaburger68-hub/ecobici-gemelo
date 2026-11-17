"""
datos_gemelo.py - Lectura y preparación de datos del gemelo digital Ecobici

  - estaciones (estaciones_seleccionadas.csv)
  - viajes históricos de los últimos MESES_HISTORIA meses  -> perfil base por bloque de 15 min
  - clima por hora y factores de clima                      -> f_clima
  - lecturas del feed GBFS                                  -> panel por minuto, eventos, camiones
  - estado y clima en vivo (opcional)

Las lecturas del feed y los viajes se guardan en cache_gemelo/ para no releer
todo en cada corrida; si aparecen archivos nuevos se leen sólo esos.
"""
import glob
import json
import os
import pickle
import re
import ssl
import urllib.request

import numpy as np
import pandas as pd

import config_gemelo as cfg

BLOQUES_DIA = 96
MIN_DIA = 1440
FESTIVOS = pd.DatetimeIndex(pd.to_datetime(cfg.FESTIVOS))


# =====================================================================
# Utilidades
# =====================================================================
def normalizar_codigo(s):
    """'64' -> '064', ' 026 ' -> '026', '107-108' queda igual."""
    s = pd.Series(s).astype(str).str.strip()
    return s.where(~s.str.fullmatch(r"\d{1,2}"), s.str.zfill(3))


def es_habil(fechas):
    f = pd.DatetimeIndex(pd.to_datetime(fechas)).normalize()
    return np.asarray((f.dayofweek < 5) & ~f.isin(FESTIVOS))


def tipo_idx(fecha):
    """0 = día hábil, 1 = fin de semana o festivo."""
    return 0 if es_habil([fecha])[0] else 1


def utc_a_local(s):
    t = pd.to_datetime(s, errors="coerce")
    try:
        return t.dt.tz_localize("UTC").dt.tz_convert(cfg.ZONA).dt.tz_localize(None)
    except Exception:   # sin base de zonas horarias: CDMX es UTC-6 todo el año desde 2022
        return t - pd.Timedelta(hours=6)


def bloque_de(t):
    """Índice del bloque de 15 min dentro del día (0..95)."""
    t = pd.Timestamp(t)
    return (t.hour * 60 + t.minute) // 15


def _firma(archivos):
    return [(a, os.path.getsize(a), os.path.getmtime(a)) for a in archivos]


def _cargar_cache(nombre):
    ruta = os.path.join(cfg.CARPETA_CACHE, nombre)
    if os.path.isfile(ruta):
        try:
            with open(ruta, "rb") as fh:
                return pickle.load(fh)
        except Exception:
            return None
    return None


def _guardar_cache(nombre, obj):
    os.makedirs(cfg.CARPETA_CACHE, exist_ok=True)
    with open(os.path.join(cfg.CARPETA_CACHE, nombre), "wb") as fh:
        pickle.dump(obj, fh)


# =====================================================================
# Estaciones
# =====================================================================
def leer_estaciones(archivo=cfg.ARCHIVO_ESTACIONES):
    if not os.path.isfile(archivo):
        raise SystemExit(f"No encontré {archivo} en {os.getcwd()}")
    e = pd.read_csv(archivo, dtype={"code": str, "station_id": str})
    e["code"] = normalizar_codigo(e["code"]).values
    e["station_id"] = e["station_id"].astype(str).str.strip()
    if "perfil" not in e:
        e["perfil"] = "Equilibrada"
    if "name" in e:
        e["nombre_corto"] = e["name"].astype(str).str.replace(r"^CE-\S+\s*", "", regex=True)
    else:
        e["nombre_corto"] = e["code"]
    e["kappa"] = cfg.KAPPA
    if os.path.isfile(cfg.ARCHIVO_KAPPA):
        k = pd.read_csv(cfg.ARCHIVO_KAPPA, dtype={"code": str})
        k["code"] = normalizar_codigo(k["code"]).values
        e["kappa"] = e["code"].map(dict(zip(k["code"], k["kappa"]))).fillna(cfg.KAPPA)
        print(f"kappa por estación leído de {cfg.ARCHIVO_KAPPA}")
    return e.reset_index(drop=True)


# =====================================================================
# Clima
# =====================================================================
CAT_LLUVIA = ["sin lluvia", "ligera (<1 mm/h)", "moderada (1-4 mm/h)", "fuerte (≥4 mm/h)"]
CAT_PREVIA = ["seco antes", "llovió en las 3 h previas"]
CAT_TEMP_ORDEN = ["mucho más frío (< −3 °C)", "más frío (−3 a −1 °C)", "normal (±1 °C)",
                  "más cálido (1 a 3 °C)", "mucho más cálido (> 3 °C)"]
CAT_VIENTO = ["< 5 km/h", "5-10 km/h", "10-15 km/h", "≥ 15 km/h"]
TIPO_ES = {0: "hábil", 1: "fin de semana"}
DEMANDA_ES = {"ret": "retiros", "dev": "arribos"}


def clima_por_hora(clima):
    """
    Una fila por periodo [H, H+1) en hora local, igual que clima_demanda.py:
    lluvia de la fila H+1 (Open-Meteo acumula la hora anterior), temperatura y
    viento promedio de H y H+1, lluvia de las 3 h previas, temperatura respecto
    de lo normal para ese mes y hora, y si la hora es "seca".
    """
    c = clima.copy()
    c["fecha_hora_local"] = pd.to_datetime(c["fecha_hora_local"])
    c = c.drop_duplicates("fecha_hora_local", keep="last").set_index("fecha_hora_local").sort_index()
    c = c.reindex(pd.date_range(c.index.min(), c.index.max(), freq="h"))
    sig = c.shift(-1)
    p = pd.DataFrame(index=c.index)
    p["precipitacion_mm"] = sig["precipitacion_mm"]
    p["temperatura_c"] = (c["temperatura_c"] + sig["temperatura_c"]) / 2 if "temperatura_c" in c else np.nan
    p["viento_kmh"] = (c["viento_kmh"] + sig["viento_kmh"]) / 2 if "viento_kmh" in c else np.nan
    p["lluvia_previa_mm"] = p["precipitacion_mm"].shift(1).rolling(3, min_periods=1).sum()
    mes, h = p.index.to_period("M"), p.index.hour
    p["temp_dif_c"] = p["temperatura_c"] - p.groupby([mes, h])["temperatura_c"].transform("mean")
    p["lluvia_cat"] = pd.cut(p["precipitacion_mm"], [-np.inf, cfg.UMBRAL_LLUVIA, 1, 4, np.inf],
                             right=False, labels=CAT_LLUVIA).astype(object)
    p["previa_cat"] = np.where(p["lluvia_previa_mm"] >= cfg.UMBRAL_LLUVIA_PREVIA, CAT_PREVIA[1], CAT_PREVIA[0])
    p["temp_cat"] = pd.cut(p["temp_dif_c"], [-np.inf, -3, -1, 1, 3, np.inf], labels=CAT_TEMP_ORDEN).astype(object)
    p["viento_cat"] = pd.cut(p["viento_kmh"], [-np.inf, 5, 10, 15, np.inf], right=False,
                             labels=CAT_VIENTO).astype(object)
    seco = ((p["precipitacion_mm"] < cfg.UMBRAL_LLUVIA)
            & (p["lluvia_previa_mm"] < cfg.UMBRAL_LLUVIA_PREVIA)).astype("boolean")
    seco[p["precipitacion_mm"].isna()] = pd.NA          # sin dato de lluvia: se decide después
    p["seco"] = seco
    p.index.name = "hora"
    return p


def leer_clima(extra=None):
    """
    Clima por hora (DataFrame indexado por el inicio de la hora) o None si no hay datos.
    `extra` (descarga de Open-Meteo) completa las horas que no están en el archivo; si una hora
    está en ambos, gana el archivo (lo registrado), porque clima_por_hora se queda con la última.
    """
    partes = []
    if extra is not None:
        partes.append(extra)
    if os.path.isfile(cfg.ARCHIVO_CLIMA):
        partes.append(pd.read_csv(cfg.ARCHIVO_CLIMA, parse_dates=["fecha_hora_local"]))
    elif extra is None:
        print(f"Aviso: no encontré {cfg.ARCHIVO_CLIMA}; el clima se toma como normal (factor 1)")
    if not partes:
        return None
    return clima_por_hora(pd.concat(partes, ignore_index=True))


def tabla_factores_clima():
    """Diccionario (tipo, demanda, variable, categoría) -> factor, desde clima_demanda.py."""
    if not os.path.isfile(cfg.ARCHIVO_FACTORES_CLIMA):
        print(f"Aviso: no encontré {cfg.ARCHIVO_FACTORES_CLIMA}; factores de clima = 1")
        return {}
    f = pd.read_csv(cfg.ARCHIVO_FACTORES_CLIMA)
    out = {}
    for _, r in f.iterrows():
        if r["variable"] == "base":
            continue
        fac = r["factor"]
        nota = str(r.get("nota", ""))
        if not np.isfinite(fac) or "pocos datos" in nota:
            fac = 1.0
        out[(r["tipo_dia"], r["demanda"], r["variable"], r["categoria"])] = float(fac)
    return out


def factores_por_hora(clima, tabla):
    """
    DataFrame indexado por hora con columnas f_ret_0, f_dev_0 (hábil) y f_ret_1,
    f_dev_1 (fin de semana): producto de los factores de lluvia, lluvia previa,
    temperatura y viento. Horas sin clima o categorías sin factor -> 1.
    """
    if clima is None or not tabla:
        return pd.DataFrame(columns=["f_ret_0", "f_dev_0", "f_ret_1", "f_dev_1"], dtype=float)
    out = pd.DataFrame(index=clima.index)
    variables = {"lluvia": "lluvia_cat", "lluvia previa": "previa_cat", "temperatura": "temp_cat",
                 "viento": "viento_cat"}
    for t in (0, 1):
        for e in ("ret", "dev"):
            f = np.ones(len(clima))
            for var, col in variables.items():
                f *= clima[col].map(lambda c: tabla.get((TIPO_ES[t], DEMANDA_ES[e], var, c), 1.0)).astype(float).values
            out[f"f_{e}_{t}"] = f
    return out


def pronostico_clima_en_vivo():
    """Clima de ayer, hoy y mañana desde Open-Meteo (para el modo en vivo)."""
    try:
        import clima_ecobici as ce
        base = {"latitude": ce.LAT, "longitude": ce.LON, "timezone": "GMT",
                "hourly": ",".join(ce.VARIABLES), "past_days": 16, "forecast_days": 2}   # cubre la ventana
        df = ce.completar(ce.a_tabla(ce.pedir(ce.URL_PRONOSTICO, base)["hourly"], "pronostico"))
        return df
    except Exception as e:
        print(f"Aviso: no pude traer el pronóstico del clima ({e}); se usa el clima guardado")
        return None


def clima_reciente():
    """
    Para reproducción: si al archivo de clima le faltan las horas recientes (GitHub lo actualiza
    una vez por ejecución), las trae de Open-Meteo. Sin internet, devuelve None y se usa el archivo.
    """
    if os.path.isfile(cfg.ARCHIVO_CLIMA):
        try:
            ult = pd.to_datetime(pd.read_csv(cfg.ARCHIVO_CLIMA, usecols=["fecha_hora_utc"])["fecha_hora_utc"]).max()
            if ult >= pd.Timestamp.now(tz="UTC").tz_localize(None).floor("h") - pd.Timedelta(hours=1):
                return None                       # el archivo ya está al día
        except Exception:
            pass
    return pronostico_clima_en_vivo()


# =====================================================================
# Viajes históricos -> perfil base
# =====================================================================
COLUMNAS_VIAJES = {
    "bici": ["Bici"],
    "est_ret": ["Ciclo_Estacion_Retiro", "Ciclo_EstacionRetiro"],
    "est_arr": ["Ciclo_EstacionArribo", "Ciclo_Estacion_Arribo"],
    "f_ret": ["Fecha_Retiro"], "h_ret": ["Hora_Retiro"],
    "f_arr": ["Fecha_Arribo"], "h_arr": ["Hora_Arribo"],
}


def _fecha_hora(f, h):
    s = f.astype(str).str.strip() + " " + h.astype(str).str.strip()
    t = pd.to_datetime(s, format="%d/%m/%Y %H:%M:%S", errors="coerce")
    if t.isna().mean() > 0.5:
        t = pd.to_datetime(s, format="mixed", dayfirst=True, errors="coerce")
    return t


def buscar_viajes(entradas=cfg.VIAJES):
    archivos = []
    for e in entradas:
        if os.path.isdir(e):
            archivos += glob.glob(os.path.join(e, "**", "*.csv"), recursive=True)
        else:
            archivos += glob.glob(e)
    return sorted(set(os.path.normpath(a) for a in archivos))


def _leer_archivo_viajes(archivo, codigos, chunksize=500_000):
    cab = pd.read_csv(archivo, nrows=0, encoding_errors="replace")
    cab.columns = cab.columns.str.strip().str.lstrip("﻿")
    nombres = {}
    for nuestro, posibles in COLUMNAS_VIAJES.items():
        hallado = [c for c in posibles if c in cab.columns]
        if not hallado and nuestro != "bici":
            print(f"  Aviso: {archivo} no tiene la columna {posibles[0]}; se omite")
            return None, None
        if hallado:
            nombres[hallado[0]] = nuestro
    partes, sistema = [], []
    lector = pd.read_csv(archivo, dtype=str, chunksize=chunksize, encoding_errors="replace",
                         usecols=lambda c: c.strip().lstrip("﻿") in nombres)
    for ch in lector:
        ch.columns = ch.columns.str.strip().str.lstrip("﻿")
        ch = ch.rename(columns=nombres)
        t_ret = _fecha_hora(ch["f_ret"], ch["h_ret"])
        t_arr = _fecha_hora(ch["f_arr"], ch["h_arr"])
        sistema.append(t_ret.dt.normalize().value_counts())
        bici = ch["bici"] if "bici" in ch else pd.Series("", index=ch.index)
        er = pd.Series(normalizar_codigo(ch["est_ret"]).values, index=ch.index)
        ea = pd.Series(normalizar_codigo(ch["est_arr"]).values, index=ch.index)
        mr = er.isin(codigos) & t_ret.notna()
        ma = ea.isin(codigos) & t_arr.notna() & (t_arr >= t_ret)
        partes.append(pd.DataFrame({"bici": bici[mr], "code": er[mr], "t": t_ret[mr], "evento": "ret"}))
        partes.append(pd.DataFrame({"bici": bici[ma], "code": ea[ma], "t": t_arr[ma], "evento": "dev"}))
    ev = pd.concat(partes, ignore_index=True)
    sistema = pd.concat(sistema).groupby(level=0).sum()
    return ev, sistema


def leer_viajes(est):
    """Eventos (retiros y devoluciones) de las 30 estaciones en todos los archivos de viajes."""
    archivos = buscar_viajes()
    if not archivos:
        raise SystemExit(f"No encontré archivos de viajes ({', '.join(cfg.VIAJES)}) en {os.getcwd()}")
    firma = _firma(archivos)
    cache = _cargar_cache("viajes_30.pkl")
    if cache is not None and cache.get("firma") == firma and cache.get("codigos") == sorted(est["code"]):
        return cache["eventos"], cache["sistema"]
    codigos = set(est["code"])
    eventos, sistemas = [], {}
    for k, a in enumerate(archivos):
        print(f"Leyendo viajes {a} ({k + 1} de {len(archivos)})")
        ev, sis = _leer_archivo_viajes(a, codigos)
        if ev is not None:
            eventos.append(ev)
            sistemas[a] = sis
    if not eventos:
        raise SystemExit("Ningún archivo tenía el formato de viajes de Ecobici")
    ev = pd.concat(eventos, ignore_index=True).drop_duplicates(["bici", "code", "t", "evento"])
    ev = ev.drop(columns="bici").reset_index(drop=True)
    sistema = pd.DataFrame(sistemas).fillna(0).max(axis=1)   # un día en dos archivos: no se suma dos veces
    _guardar_cache("viajes_30.pkl", {"firma": firma, "codigos": sorted(est["code"]),
                                     "eventos": ev, "sistema": sistema})
    return ev, sistema


def dias_historia(sistema, fecha_ref, meses=cfg.MESES_HISTORIA):
    """Días válidos de los últimos `meses` meses completos publicados antes de fecha_ref."""
    validos = sistema[sistema >= cfg.MIN_FRAC_DIA * sistema.median()].index
    validos = pd.DatetimeIndex(sorted(validos))
    validos = validos[validos < pd.Timestamp(fecha_ref).normalize()]
    por_mes = pd.Series(1, index=validos).groupby(validos.to_period("M")).sum()
    completos = por_mes[por_mes >= cfg.MIN_DIAS_MES].index
    elegidos = list(completos[-meses:])
    if len(elegidos) < meses:
        print(f"Aviso: sólo hay {len(elegidos)} mes(es) completo(s) de viajes antes de {fecha_ref:%Y-%m-%d}")
    if not elegidos:
        raise SystemExit("No hay meses completos de viajes para el perfil base")
    dias = validos[validos.to_period("M").isin(elegidos)]
    print(f"Historia de viajes: {', '.join(str(m) for m in elegidos)} ({len(dias)} días válidos)")
    return dias


def perfil_base(ev, dias, est, clima):
    """
    Paso 1.1: lambda_base[t, i, b] = 4 * s[b] * lambda_h[i, h]  (eventos por hora)
    t: 0 hábil, 1 fin de semana; i: estación; b: bloque de 15 min (0..95).
    Si SOLO_SECO, sólo se usan horas sin lluvia (ni en la hora ni en las 3 h previas).
    Devuelve (lam_ret, lam_dev, tabla) con lam_* de forma (2, I, 96).
    """
    I = len(est)
    idx = {c: i for i, c in enumerate(est["code"])}
    horas = list(cfg.HORAS_SERVICIO)

    # Día-hora utilizables
    dh = pd.DataFrame([(d, h) for d in dias for h in horas], columns=["fecha", "h"])
    dh["t"] = np.where(es_habil(dh["fecha"]), 0, 1)
    dh["usar"] = True
    if cfg.SOLO_SECO:
        if clima is None:
            print("Aviso: sin clima no puedo separar horas secas; el perfil base usa todas las horas")
        else:
            inicio = dh["fecha"] + pd.to_timedelta(dh["h"], unit="h")
            seco = clima["seco"].reindex(inicio).values
            dh["usar"] = pd.Series(seco).astype("boolean").fillna(True).astype(bool).values
            print(f"Perfil base con horas secas: {dh['usar'].mean():.0%} de las horas")
    n_dias = np.zeros((2, 24))
    for (t, h), n in dh[dh["usar"]].groupby(["t", "h"]).size().items():
        n_dias[t, h] = n

    e = ev[ev["t"].dt.normalize().isin(dias)].copy()
    e["fecha"] = e["t"].dt.normalize()
    e["h"] = e["t"].dt.hour
    e = e[e["h"].isin(horas)]
    e = e.merge(dh[["fecha", "h", "t", "usar"]].rename(columns={"t": "tipo"}), on=["fecha", "h"], how="left")
    e = e[e["usar"].fillna(False).astype(bool)]
    n = np.zeros((2, 2, I, BLOQUES_DIA))           # [tipo, evento(0 ret, 1 dev), estación, bloque]
    np.add.at(n, (e["tipo"].astype(int).values, (e["evento"] == "dev").astype(int).values,
                  e["code"].map(idx).astype(int).values,
                  ((e["t"].dt.hour * 60 + e["t"].dt.minute) // 15).astype(int).values), 1)

    n_h = n.reshape(2, 2, I, 24, 4).sum(-1)        # por hora
    with np.errstate(invalid="ignore", divide="ignore"):
        lam_h = np.where(n_dias[:, None, None, :] > 0, n_h / n_dias[:, None, None, :], 0.0)

    # s: reparto dentro de la hora
    n4 = n.reshape(2, 2, I, 24, 4)
    if cfg.S_MODO == "estacion":
        grupo_n4 = n4
    elif cfg.S_MODO == "perfil":
        grupo_n4 = np.zeros_like(n4)
        for p in est["perfil"].unique():
            m = (est["perfil"] == p).values
            grupo_n4[:, :, m] = n4[:, :, m].sum(2, keepdims=True)
    else:
        grupo_n4 = np.broadcast_to(n4.sum(2, keepdims=True), n4.shape)
    tot = grupo_n4.sum(-1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.where(tot > 0, grupo_n4 / tot, 0.25)
    lam = (4 * s * lam_h[..., None]).reshape(2, 2, I, BLOQUES_DIA)

    filas = []
    for t in (0, 1):
        for i, c in enumerate(est["code"]):
            for b in range(BLOQUES_DIA):
                h = b // 4
                if h in horas:
                    filas.append((c, "habil" if t == 0 else "fin_semana", h, b % 4 + 1,
                                  f"{h:02d}:{(b % 4) * 15:02d}", lam[t, 0, i, b], lam[t, 1, i, b],
                                  s.reshape(2, 2, I, BLOQUES_DIA)[t, 0, i, b]))
    tabla = pd.DataFrame(filas, columns=["code", "tipo", "hora", "bloque", "inicio", "lambda_retiro_base",
                                         "lambda_devol_base", "s_retiro"])
    return lam[:, 0], lam[:, 1], tabla


def leer_perfil_guardado(est, archivo=cfg.ARCHIVO_PERFIL_BASE):
    """Perfil base ya calculado (perfil_base_15min.csv), para correr sin los archivos de viajes."""
    t = pd.read_csv(archivo, dtype={"code": str})
    t["code"] = normalizar_codigo(t["code"]).values
    I = len(est)
    idx = {c: i for i, c in enumerate(est["code"])}
    faltan = set(est["code"]) - set(t["code"])
    if faltan:
        print(f"Aviso: el perfil guardado no tiene las estaciones {', '.join(sorted(faltan))} (tasa base 0)")
    t = t[t["code"].isin(idx)]
    lam_r = np.zeros((2, I, BLOQUES_DIA))
    lam_d = np.zeros((2, I, BLOQUES_DIA))
    ti = np.where(t["tipo"] == "habil", 0, 1)
    ii = t["code"].map(idx).astype(int).values
    bb = (t["hora"].astype(int) * 4 + t["bloque"].astype(int) - 1).values
    lam_r[ti, ii, bb] = t["lambda_retiro_base"].astype(float).values
    lam_d[ti, ii, bb] = t["lambda_devol_base"].astype(float).values
    print(f"Perfil base leído de {archivo} (sin archivos de viajes)")
    return lam_r, lam_d, t


# =====================================================================
# Feed GBFS -> panel por minuto
# =====================================================================
COLS_FEED = ["lectura_utc", "station_id", "num_bikes_available", "num_docks_available",
             "is_renting", "is_returning", "last_reported"]


def _fecha_en_ruta(ruta):
    m = re.findall(r"\d{4}-\d{2}-\d{2}", ruta.replace("\\", "/"))
    return pd.Timestamp(m[-1]) if m else None


def leer_feed(est, carpeta=cfg.CARPETA_STATUS, desde=None):
    """
    Lecturas de las 30 estaciones en hora local. Usa caché y lee sólo archivos nuevos o modificados.
    desde: si se indica, se omiten los archivos cuya fecha (en el nombre o la carpeta) es anterior.
    """
    archivos = sorted(glob.glob(os.path.join(carpeta, "**", "*.csv"), recursive=True)
                      + glob.glob(os.path.join(carpeta, "**", "*.csv.gz"), recursive=True))
    if desde is not None:
        lim = pd.Timestamp(desde).normalize() - pd.Timedelta(days=1)    # margen por el desfase UTC
        archivos = [a for a in archivos if (_fecha_en_ruta(a) is None or _fecha_en_ruta(a) >= lim)]
    if not archivos:
        raise SystemExit(f"No hay lecturas del feed en {carpeta}")
    ids = set(est["station_id"])
    cache = _cargar_cache("feed_30.pkl") or {}
    if cache.get("ids") != sorted(ids):
        cache = {}
    firmas_prev = cache.get("firmas", {})
    datos = cache.get("datos")
    firmas = {a: (os.path.getsize(a), os.path.getmtime(a)) for a in archivos}
    cambiados = [a for a in archivos if firmas_prev.get(a) != firmas[a]]
    if datos is not None:
        datos = datos[datos["archivo"].isin(set(archivos) - set(cambiados))]
    nuevos = []
    for k, a in enumerate(cambiados):
        if k % 50 == 0:
            print(f"Leyendo lecturas del feed: {k + 1} de {len(cambiados)} archivos nuevos")
        try:
            d = pd.read_csv(a, usecols=lambda c: c in COLS_FEED, dtype={"station_id": str})
        except Exception as e:
            print(f"Aviso: no pude leer {a}: {e}")
            continue
        d = d[d["station_id"].astype(str).str.strip().isin(ids)].copy()
        d["archivo"] = a
        nuevos.append(d)
    if nuevos:
        nuevos = pd.concat(nuevos, ignore_index=True)
        nuevos["t"] = utc_a_local(nuevos["lectura_utc"])
        nuevos = nuevos.drop(columns="lectura_utc")
        datos = nuevos if datos is None else pd.concat([datos, nuevos], ignore_index=True)
    if datos is None or datos.empty:
        raise SystemExit("Las lecturas del feed no tienen ninguna de las 30 estaciones")
    _guardar_cache("feed_30.pkl", {"ids": sorted(ids), "firmas": firmas, "datos": datos})
    inicio = pd.Timestamp(cfg.INICIO_FEED)
    if desde is not None:
        inicio = max(inicio, pd.Timestamp(desde).normalize())
    return datos[datos["t"] >= inicio]


class Panel:
    """
    Estado de las 30 estaciones minuto a minuto y eventos derivados del feed.

    Arreglos (I estaciones x T minutos, T = días * 1440):
      B, D        bicis y anclajes disponibles (rellenados hasta MAX_RELLENO_MIN; NaN = sin dato)
      renta, recibe
      dato        True si el minuto tiene dato confiable
      ret, dev    retiros y devoluciones detectados en ese minuto (diferencias entre reportes)
      camion      salto atribuido al camión del operador (con signo)
    Por bloque de 15 min (I x días x 96): bret, bdev, bexr (min con bicis), bexd (min con anclajes), bcam
    """

    def __init__(self, lect, est, umbral_camion=cfg.UMBRAL_CAMION):
        self.est = est
        I = len(est)
        idx = {s: i for i, s in enumerate(est["station_id"])}
        d = lect.copy()
        d["station_id"] = d["station_id"].astype(str).str.strip()
        d["m"] = d["t"].dt.floor("min")
        d = d.dropna(subset=["m"]).sort_values(["station_id", "t"]).drop_duplicates(["station_id", "m"], keep="last")
        self.t_ini = d["m"].min().normalize()
        t_fin = d["m"].max().normalize() + pd.Timedelta(days=1)
        self.n_dias = int((t_fin - self.t_ini) / pd.Timedelta(days=1))
        T = self.n_dias * MIN_DIA
        self.T = T
        self.fechas = pd.date_range(self.t_ini, periods=self.n_dias, freq="D")
        pos = ((d["m"] - self.t_ini) / pd.Timedelta(minutes=1)).astype(int).values
        ii = d["station_id"].map(idx).astype(int).values

        crudo = {}
        for nombre, col in [("B", "num_bikes_available"), ("D", "num_docks_available"),
                            ("renta", "is_renting"), ("recibe", "is_returning"), ("lr", "last_reported")]:
            a = np.full((I, T), np.nan)
            if col in d:
                a[ii, pos] = pd.to_numeric(d[col], errors="coerce").values
            crudo[nombre] = a
        obs = ~np.isnan(crudo["B"])

        def rellenar(a):
            return pd.DataFrame(a.T).ffill(limit=cfg.MAX_RELLENO_MIN).values.T

        self.B = rellenar(crudo["B"]).astype(np.float32)
        self.D = rellenar(crudo["D"]).astype(np.float32)
        self.renta = np.nan_to_num(rellenar(crudo["renta"]), nan=1.0) != 0
        self.recibe = np.nan_to_num(rellenar(crudo["recibe"]), nan=1.0) != 0
        self.dato = ~np.isnan(self.B) & ~np.isnan(self.D)

        # Eventos por diferencias entre reportes distintos (last_reported cambia)
        self.ret = np.zeros((I, T), np.int16)
        self.dev = np.zeros((I, T), np.int16)
        self.camion = np.zeros((I, T), np.int16)
        self.saltos = []
        for i in range(I):
            p = np.flatnonzero(obs[i])
            if len(p) < 2:
                continue
            lr = crudo["lr"][i, p]
            b = crudo["B"][i, p]
            if np.all(np.isnan(lr)):
                nuevo = np.r_[True, np.diff(b) != 0]
            else:
                nuevo = np.r_[True, (lr[1:] != lr[:-1]) | np.isnan(lr[1:])]
            p, b = p[nuevo], b[nuevo]
            db = np.diff(b).astype(int)
            gap = np.diff(p)
            dest = p[1:]
            hueco = gap > cfg.MAX_HUECO_MIN
            for a0, a1 in zip(p[:-1][hueco], dest[hueco]):   # la estación no reportó: sin dato
                self.dato[i, a0 + 1:a1] = False
            cam = ~hueco & (np.abs(db) > umbral_camion)
            usu = ~hueco & ~cam
            self.camion[i, dest[cam]] = db[cam]
            np.add.at(self.ret[i], dest[usu], np.maximum(-db[usu], 0))
            np.add.at(self.dev[i], dest[usu], np.maximum(db[usu], 0))
            self.saltos.append(db[~hueco & (db != 0)])
        self.saltos = np.concatenate(self.saltos) if self.saltos else np.array([], int)

        # Exposición: minutos en que la estación podía atender
        Bz = np.nan_to_num(self.B)
        Dz = np.nan_to_num(self.D)
        exr = self.dato & (Bz > 0) & self.renta
        exd = self.dato & (Dz > 0) & self.recibe

        def por_bloque(a):
            return a.reshape(I, self.n_dias, BLOQUES_DIA, 15).sum(-1)

        self.bret = por_bloque(self.ret.astype(np.int32))
        self.bdev = por_bloque(self.dev.astype(np.int32))
        self.bexr = por_bloque(exr.astype(np.int32))
        self.bexd = por_bloque(exd.astype(np.int32))
        self.bcam = por_bloque((self.camion != 0).astype(np.int32))
        servicio = np.zeros(MIN_DIA, bool)
        servicio[min(cfg.HORAS_SERVICIO) * 60:(max(cfg.HORAS_SERVICIO) + 1) * 60] = True
        cob = self.dato.reshape(I, self.n_dias, MIN_DIA)[:, :, servicio].mean(axis=(0, 2))
        self.cobertura_dia = pd.Series(cob, index=self.fechas)

    # --- índices de tiempo ---
    def pos(self, t):
        return int((pd.Timestamp(t).floor("min") - self.t_ini) / pd.Timedelta(minutes=1))

    def dia(self, fecha):
        return int((pd.Timestamp(fecha).normalize() - self.t_ini) / pd.Timedelta(days=1))

    def dias_ventana(self, fecha, W):
        """Índices de los W días hábiles con datos anteriores a `fecha`."""
        f = pd.Timestamp(fecha).normalize()
        cand = [k for k, d in enumerate(self.fechas)
                if d < f and es_habil([d])[0] and self.cobertura_dia.iloc[k] >= cfg.MIN_COBERTURA_DIA]
        return cand[-W:]

    def ultima_lectura(self):
        hay = np.flatnonzero(self.dato.any(0))
        return self.t_ini + pd.Timedelta(minutes=int(hay[-1])) if len(hay) else None

    def resumen(self):
        ok = self.cobertura_dia
        txt = [f"Feed: {self.fechas[0]:%Y-%m-%d} a {self.fechas[-1]:%Y-%m-%d}",
               "Días con datos (cobertura 05-24 h): " + ", ".join(
                   f"{d:%d/%m} {c:.0%}" for d, c in ok.items() if c > 0)]
        n_cam = int((self.camion != 0).sum())
        txt.append(f"Eventos detectados: {int(self.ret.sum())} retiros, {int(self.dev.sum())} devoluciones, "
                   f"{n_cam} saltos de camión (> {cfg.UMBRAL_CAMION} bicis)")
        return "\n".join(txt)


# =====================================================================
# En vivo
# =====================================================================
def _contexto_ssl():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def _json(url):
    with urllib.request.urlopen(url, timeout=20, context=_contexto_ssl()) as r:
        return json.load(r)


def estado_en_vivo(est):
    """Lee station_status ahora. Devuelve (hora local, DataFrame con B, D, renta, recibe por estación)."""
    indice = _json(cfg.URL_GBFS)
    datos = indice["data"]
    feeds = datos["feeds"] if "feeds" in datos else next(iter(datos.values()))["feeds"]
    url = next(f["url"] for f in feeds if f["name"] == "station_status")
    st = pd.DataFrame(_json(url)["data"]["stations"])
    st["station_id"] = st["station_id"].astype(str)
    st = est[["station_id"]].merge(st, on="station_id", how="left")
    ahora = utc_a_local(pd.Series([pd.Timestamp.now(tz="UTC").tz_localize(None)])).iloc[0].floor("min")
    return ahora, st
