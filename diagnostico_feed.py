"""
diagnostico_feed.py - ¿Por qué la cobertura del feed es baja?

Separa dos causas:
  A) El recolector no leyó en algunos minutos (huecos de GitHub Actions o del computador).
  B) El recolector sí leyó, pero las estaciones no actualizaron su reporte (last_reported)
     y el gemelo marcó esos minutos como "sin dato".

Uso (en la carpeta del gemelo):  py -3.14 diagnostico_feed.py
Copia y pega lo que imprime.
"""
import numpy as np
import pandas as pd

import config_gemelo as cfg
from datos_gemelo import Panel, leer_estaciones, leer_feed

est = leer_estaciones()
d = leer_feed(est)
d["m"] = d["t"].dt.floor("min")
d["fecha"] = d["m"].dt.normalize()
serv = d["m"].dt.hour.between(min(cfg.HORAS_SERVICIO), max(cfg.HORAS_SERVICIO))
minutos_servicio = 60 * len(cfg.HORAS_SERVICIO)

# A) Minutos en que el recolector leyó (al menos una estación)
leidos = d[serv].groupby("fecha")["m"].nunique() / minutos_servicio
# Cobertura que usa el gemelo
p = Panel(d, est)
tabla = pd.DataFrame({"recolector_leyo": leidos, "cobertura_gemelo": p.cobertura_dia}).fillna(0)
print("\nCobertura por día (05:00-24:00):")
print((100 * tabla).round(0).astype(int).astype(str).add(" %").to_string())

# Huecos más largos del recolector
m = np.sort(d["m"].unique())
saltos = pd.Series(np.diff(m), index=m[:-1]) / pd.Timedelta(minutes=1)
grandes = saltos[saltos > 5].sort_values(ascending=False)
print(f"\nHuecos del recolector de más de 5 min: {len(grandes)}")
for t, s in grandes.head(12).items():
    print(f"  desde {pd.Timestamp(t):%d/%m %H:%M}  {s:.0f} min sin lecturas")

# B) Antigüedad del reporte de cada estación al momento de la lectura
lr = pd.to_numeric(d["last_reported"], errors="coerce")
if lr.median() > 1e11:
    lr = lr / 1000                                   # milisegundos -> segundos
utc = d["t"] + pd.Timedelta(hours=6)                 # CDMX = UTC-6
edad = (utc - pd.to_datetime(lr, unit="s")).dt.total_seconds() / 60
edad = edad[serv]
print("\nAntigüedad del último reporte de la estación al leer el feed (minutos):")
print("  percentiles 50 / 75 / 90 / 99:  " + " / ".join(f"{edad.quantile(q):.1f}" for q in (0.5, 0.75, 0.9, 0.99)))
for lim in (5, 10, 30, 60):
    print(f"  lecturas con reporte de más de {lim:>2} min: {100 * (edad > lim).mean():.1f} %")

# Cada cuánto cambia last_reported en una misma estación
x = d[serv].sort_values(["station_id", "t"])
cambia = x.groupby("station_id")["last_reported"].transform(lambda s: s.ne(s.shift()))
t_cambio = x.loc[cambia, ["station_id", "t"]]
inter = t_cambio.groupby("station_id")["t"].diff().dt.total_seconds().dropna() / 60
print("\nMinutos entre reportes nuevos de una misma estación:")
print("  percentiles 50 / 75 / 90 / 99:  " + " / ".join(f"{inter.quantile(q):.1f}" for q in (0.5, 0.75, 0.9, 0.99)))
print(f"  intervalos de más de {cfg.MAX_HUECO_MIN} min (el gemelo los marca sin dato): {100 * (inter > cfg.MAX_HUECO_MIN).mean():.1f} %")
print(f"\nLecturas: {len(d):,} · estaciones: {d['station_id'].nunique()} · "
      f"primera {d['t'].min():%d/%m %H:%M} · última {d['t'].max():%d/%m %H:%M} (hora CDMX)")
