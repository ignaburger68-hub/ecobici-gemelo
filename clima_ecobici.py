"""
clima_ecobici.py - Clima por hora en el centroide de las 30 estaciones (Open-Meteo)
Proyecto Simulación · Gemelo digital Ecobici

Variables (una fila por hora):
    precipitacion_mm   lluvia + otras precipitaciones de esa hora (mm)
    temperatura_c      temperatura a 2 m (°C)
    viento_kmh         viento a 10 m (km/h)
    codigo_clima       código WMO (0 despejado, 61-65 lluvia, 95 tormenta, ...)
    llueve             1 si precipitacion_mm >= UMBRAL_LLUVIA, 0 si no

Uso:
    # Histórico de una fecha X a una fecha Y (ambas incluidas)
    py -3.14 clima_ecobici.py historico 2026-08-01 2026-10-31
    # Desde una fecha hasta hoy
    py -3.14 clima_ecobici.py historico 2026-10-01
    # Sin fechas: los últimos 90 días (o los que indiques con --dias)
    py -3.14 clima_ecobici.py historico
    py -3.14 clima_ecobici.py historico --dias 120

    Cada consulta se guarda en su propio archivo:
        datos/clima/clima_AAAA-MM-DD_a_AAAA-MM-DD.csv
    y además se acumula en datos/clima/clima_horario.csv (el que usa el modelo).

    # Tiempo real: una lectura ahora -> datos/clima/clima_actual.csv
    py -3.14 clima_ecobici.py actual
    # o una lectura cada 15 minutos hasta cerrar la ventana (Ctrl+C)
    py -3.14 clima_ecobici.py actual --loop

    Volver a correr "historico" no borra nada: agrega las horas nuevas y
    actualiza las existentes. Sirve también para completar días recientes.

Uso desde Python (para el modelo):
    from clima_ecobici import leer_clima, agregar_clima
    clima = leer_clima()                                   # tabla por hora
    lecturas = agregar_clima(lecturas, "lectura_utc")      # agrega columnas de clima

Requisitos: pandas, certifi  (py -3.14 -m pip install pandas certifi)
"""

import argparse
import json
import os
import ssl
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta

import pandas as pd

# ---------------------------------------------------------------------
# Parámetros
# ---------------------------------------------------------------------
LAT, LON = 19.43264, -99.15569        # centroide de las 30 estaciones
ZONA = "America/Mexico_City"
UMBRAL_LLUVIA = 0.1                   # mm/h para considerar que llueve
DIAS_POR_DEFECTO = 90
CARPETA = os.path.join("datos", "clima")
ARCHIVO_HORARIO = os.path.join(CARPETA, "clima_horario.csv")
ARCHIVO_ACTUAL = os.path.join(CARPETA, "clima_actual.csv")
INTERVALO_MIN = 15                    # minutos entre lecturas en modo --loop

URL_ARCHIVO = "https://archive-api.open-meteo.com/v1/archive"
URL_PRONOSTICO = "https://api.open-meteo.com/v1/forecast"

# Nombre en Open-Meteo -> nombre en nuestras tablas
VARIABLES = {
    "precipitation": "precipitacion_mm",
    "temperature_2m": "temperatura_c",
    "wind_speed_10m": "viento_kmh",
    "weather_code": "codigo_clima",
}
COLUMNAS = ["fecha_hora_utc", "fecha_hora_local", "fecha", "hora",
            *VARIABLES.values(), "llueve", "fuente"]


# ---------------------------------------------------------------------
# Descarga
# ---------------------------------------------------------------------
def contexto_ssl():
    """Usa los certificados actualizados de 'certifi' si está instalado."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def pedir(url, parametros, intentos=3):
    """GET a Open-Meteo y devuelve el JSON (reintenta si falla la conexión)."""
    direccion = url + "?" + urllib.parse.urlencode(parametros)
    contexto = contexto_ssl()
    for i in range(intentos):
        try:
            with urllib.request.urlopen(direccion, timeout=60, context=contexto) as r:
                return json.load(r)
        except Exception as e:
            if i == intentos - 1:
                raise RuntimeError(f"No pude descargar {url}: {e}")
            time.sleep(5)


def a_tabla(horario, fuente):
    """Convierte el bloque 'hourly' de Open-Meteo (en UTC) a nuestra tabla."""
    df = pd.DataFrame({"fecha_hora_utc": pd.to_datetime(horario["time"])})
    for nombre_api, nombre in VARIABLES.items():
        df[nombre] = pd.to_numeric(pd.Series(horario.get(nombre_api)), errors="coerce")
    df["fuente"] = fuente
    return df.dropna(subset=list(VARIABLES.values()), how="all")


def completar(df):
    """Agrega hora local, fecha, hora y la variable 'llueve'."""
    df = df.copy()
    df["fecha_hora_utc"] = pd.to_datetime(df["fecha_hora_utc"])
    local = df["fecha_hora_utc"].dt.tz_localize("UTC").dt.tz_convert(ZONA).dt.tz_localize(None)
    df["fecha_hora_local"] = local
    df["fecha"] = local.dt.date.astype(str)
    df["hora"] = local.dt.hour
    df["llueve"] = (df["precipitacion_mm"] >= UMBRAL_LLUVIA).astype(int)
    return df[COLUMNAS]


def descargar_historico(desde, hasta):
    """
    Clima por hora entre dos fechas (incluidas).
    1) Archivo histórico de Open-Meteo.
    2) Las horas que falten (los días más recientes pueden venir con
       retraso) se completan con el pronóstico, que guarda los días pasados.
    """
    base = {"latitude": LAT, "longitude": LON, "timezone": "GMT",
            "hourly": ",".join(VARIABLES)}

    print(f"Descargando histórico {desde} a {hasta} ...")
    # Se pide en UTC: la noche local del último día cae en el día UTC siguiente
    fin_utc = min(date.fromisoformat(hasta) + timedelta(days=1), date.today()).isoformat()
    arch = a_tabla(pedir(URL_ARCHIVO, {**base, "start_date": desde, "end_date": fin_utc})["hourly"],
                   "archivo")

    # Horas faltantes recientes: pronóstico con past_days (máximo 92 días)
    dias_atras = (date.today() - date.fromisoformat(desde)).days + 1
    if date.fromisoformat(hasta) >= date.today() - timedelta(days=7):
        print("Completando los días recientes con el pronóstico ...")
        pron = a_tabla(pedir(URL_PRONOSTICO, {**base, "past_days": min(dias_atras, 92),
                                             "forecast_days": 1})["hourly"], "pronostico")
        pron = pron[~pron["fecha_hora_utc"].isin(arch["fecha_hora_utc"])]
        arch = pd.concat([arch, pron], ignore_index=True)

    df = completar(arch)
    # Solo el rango pedido (en hora local) y nada del futuro
    df = df[(df["fecha"] >= desde) & (df["fecha"] <= hasta)
            & (df["fecha_hora_utc"] <= pd.Timestamp.now(tz="UTC").tz_localize(None))]
    return df.sort_values("fecha_hora_utc").reset_index(drop=True)


def descargar_actual():
    """Condiciones de ahora (Open-Meteo las entrega en intervalos de 15 min)."""
    r = pedir(URL_PRONOSTICO, {"latitude": LAT, "longitude": LON, "timezone": "GMT",
                               "current": ",".join(VARIABLES)})["current"]
    df = pd.DataFrame([{"fecha_hora_utc": pd.to_datetime(r["time"]),
                        **{nombre: r.get(api) for api, nombre in VARIABLES.items()},
                        "fuente": "actual"}])
    df = completar(df)
    df.insert(0, "lectura_utc", pd.Timestamp.now(tz="UTC").tz_localize(None).floor("s"))
    return df


# ---------------------------------------------------------------------
# Guardado
# ---------------------------------------------------------------------
def guardar_horario(nuevo, archivo=ARCHIVO_HORARIO):
    """Une con lo ya guardado; si una hora se repite, queda la versión nueva."""
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    if os.path.isfile(archivo):
        viejo = pd.read_csv(archivo, parse_dates=["fecha_hora_utc", "fecha_hora_local"])
        nuevo = pd.concat([viejo, nuevo], ignore_index=True)
    nuevo = (nuevo.drop_duplicates("fecha_hora_utc", keep="last")
             .sort_values("fecha_hora_utc").reset_index(drop=True))
    nuevo.to_csv(archivo, index=False)
    return nuevo


def guardar_actual(fila, archivo=ARCHIVO_ACTUAL):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    fila.to_csv(archivo, mode="a", header=not os.path.isfile(archivo), index=False)


# ---------------------------------------------------------------------
# Para el modelo
# ---------------------------------------------------------------------
def leer_clima(archivo=ARCHIVO_HORARIO):
    """Tabla de clima por hora, lista para usar."""
    return pd.read_csv(archivo, parse_dates=["fecha_hora_utc", "fecha_hora_local"])


def agregar_clima(df, columna_tiempo, utc=True, clima=None):
    """
    Agrega a una tabla (lecturas del feed, viajes, periodos de la simulación)
    el clima de la hora correspondiente.

    columna_tiempo: nombre de la columna con fecha y hora.
    utc=True  -> esa columna está en UTC (ej. 'lectura_utc' del recolector).
    utc=False -> está en hora local de CDMX (ej. viajes históricos).
    """
    clima = leer_clima() if clima is None else clima
    clave = "fecha_hora_utc" if utc else "fecha_hora_local"
    t = pd.to_datetime(df[columna_tiempo]).dt.floor("h")
    c = clima[[clave, *VARIABLES.values(), "llueve"]].rename(columns={clave: "_hora"})
    out = df.assign(_hora=t.values).merge(c, on="_hora", how="left").drop(columns="_hora")
    faltan = out["precipitacion_mm"].isna().mean()
    if faltan > 0:
        print(f"Aviso: {faltan:.1%} de las filas no tienen clima (fuera del rango descargado)")
    return out


# ---------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------
def resumen(df):
    print(f"{len(df)} horas, del {df['fecha'].min()} al {df['fecha'].max()}")
    print(f"Horas con lluvia: {df['llueve'].sum()} ({df['llueve'].mean():.1%})")
    print(f"Temperatura: {df['temperatura_c'].min():.1f} a {df['temperatura_c'].max():.1f} °C")
    sin_datos = df[list(VARIABLES.values())].isna().any(axis=1).sum()
    if sin_datos:
        print(f"Aviso: {sin_datos} horas con algún dato faltante")


def main():
    p = argparse.ArgumentParser(description="Clima del centroide de las 30 estaciones")
    sub = p.add_subparsers(dest="modo", required=True)

    h = sub.add_parser("historico", help="clima por hora entre dos fechas")
    h.add_argument("desde", nargs="?", help="fecha inicial AAAA-MM-DD")
    h.add_argument("hasta", nargs="?", help="fecha final AAAA-MM-DD (por defecto hoy)")
    h.add_argument("--dias", type=int, default=DIAS_POR_DEFECTO,
                   help=f"si no se da fecha inicial: cuántos días hacia atrás (por defecto {DIAS_POR_DEFECTO})")

    a = sub.add_parser("actual", help="condiciones de ahora")
    a.add_argument("--loop", action="store_true",
                   help=f"repetir cada {INTERVALO_MIN} minutos hasta Ctrl+C")
    args = p.parse_args()

    if args.modo == "historico":
        try:
            hasta = date.fromisoformat(args.hasta) if args.hasta else date.today()
            desde = (date.fromisoformat(args.desde) if args.desde
                     else hasta - timedelta(days=args.dias - 1))
        except ValueError:
            raise SystemExit("Las fechas deben tener el formato AAAA-MM-DD, por ejemplo 2026-08-01")
        if hasta > date.today():
            print(f"Aviso: no hay datos del futuro; se usa como fecha final hoy ({date.today()})")
            hasta = date.today()
        if desde > hasta:
            raise SystemExit(f"La fecha inicial ({desde}) es posterior a la final ({hasta})")

        df = descargar_historico(desde.isoformat(), hasta.isoformat())
        if df.empty:
            raise SystemExit("No llegaron datos para ese rango")
        archivo_rango = os.path.join(CARPETA, f"clima_{desde}_a_{hasta}.csv")
        os.makedirs(CARPETA, exist_ok=True)
        df.to_csv(archivo_rango, index=False)
        total = guardar_horario(df)
        resumen(df)
        print(f"Guardado en {archivo_rango}")
        print(f"Acumulado en {ARCHIVO_HORARIO} ({len(total)} horas en total)")
    else:
        while True:
            try:
                fila = descargar_actual()
                guardar_actual(fila)
                r = fila.iloc[0]
                print(f"{r['fecha_hora_local']:%Y-%m-%d %H:%M}  {r['temperatura_c']} °C  "
                      f"lluvia {r['precipitacion_mm']} mm  viento {r['viento_kmh']} km/h")
            except Exception as e:
                print("Error:", e)
            if not args.loop:
                break
            time.sleep(INTERVALO_MIN * 60)


if __name__ == "__main__":
    main()
