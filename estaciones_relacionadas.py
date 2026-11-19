#!/usr/bin/env python3
"""
estaciones_relacionadas.py
Encuentra las estaciones Ecobici que se relacionan con las 30 estaciones del
gemelo digital, usando los viajes históricos.

Una estación externa "se relaciona" con el área si intercambia viajes con ella:
  - salidas  : viajes que parten en el área y terminan en la estación externa
  - entradas : viajes que parten en la estación externa y terminan en el área

Para cada estación externa se calculan dos medidas:
  - peso_para_area : % de los viajes de frontera del área que pasan por ella
                     (qué tan importante es esa estación PARA NOSOTROS)
  - dependencia    : % de los viajes de esa estación que van o vienen del área
                     (qué tanto DEPENDE esa estación DE NOSOTROS)

Uso (en una sola línea):
    python estaciones_relacionadas.py viajes_mes1.csv [viajes_mes2.csv ...]

Opciones (al final de la línea):
    --area estaciones_seleccionadas.csv   archivo con la columna "code" de las 30
                                          estaciones (por defecto ese nombre)
    --info info_estaciones.csv            agrega nombre y distancia al centro del área
                                          (columnas name, lat, lon; el código se saca
                                          de "CE-xxx" en el nombre si no hay columna code)

Salidas (en la carpeta actual):
    estaciones_relacionadas.csv  todas las estaciones externas, ordenadas
    estaciones_clave.csv         las que cumplen los criterios de selección
    resumen_area.txt             viajes internos, de frontera y por bloque horario

Requisitos: pandas, numpy

Cambios respecto a la versión anterior:
  - El área se define con los códigos de los VIAJES (columna "code" de
    estaciones_seleccionadas.csv: 026, 010, 107-108...). Antes se usaban los
    station_id del feed GBFS (353, 240...), que son otra numeración, y el área
    terminaba siendo un grupo de estaciones distinto.
  - Con varios archivos se usan todos los meses. Antes se quedaba solo con el
    mes más frecuente.
"""
import os
import sys

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# Parámetros (ajústalos aquí)
# ---------------------------------------------------------------
ARCHIVO_AREA = "estaciones_seleccionadas.csv"   # columna "code" = códigos de los viajes

DURACION_MIN = 1          # minutos: viajes más cortos se descartan
DURACION_MAX = 180        # minutos: viajes más largos se descartan (datos sucios)
COBERTURA = 0.80          # criterio 1: estaciones que juntas cubren el 80% del flujo de frontera
DEPENDENCIA_MIN = 0.10    # criterio 2: estaciones con >=10% de sus viajes ligados al área
VIAJES_MIN_DIA = 1.0      # criterio 2 sólo aplica si la estación tiene >= 1 viaje/día con el área
MIN_FRAC_MES = 0.05       # meses con menos del 5% de los viajes del mes mayor se descartan

BLOQUES = {               # bloques horarios (hora de retiro)
    "Madrugada 0-6": range(0, 7),
    "Punta AM 7-9": range(7, 10),
    "Valle 10-16": range(10, 17),
    "Punta PM 17-19": range(17, 20),
    "Noche 20-23": range(20, 24),
}

# ---------------------------------------------------------------
# Lectura
# ---------------------------------------------------------------
COLS = ["Bici", "Ciclo_Estacion_Retiro", "Fecha_Retiro", "Hora_Retiro",
        "Ciclo_EstacionArribo", "Fecha_Arribo", "Hora_Arribo"]


def leer_viajes(rutas):
    partes = []
    for r in rutas:
        df = pd.read_csv(r, usecols=COLS, dtype=str)
        print(f"  {r}: {len(df):,} viajes")
        partes.append(df)
    v = pd.concat(partes, ignore_index=True).drop_duplicates()
    v["ini"] = pd.to_datetime(v.Fecha_Retiro + " " + v.Hora_Retiro,
                              format="%d/%m/%Y %H:%M:%S", errors="coerce")
    v["fin"] = pd.to_datetime(v.Fecha_Arribo + " " + v.Hora_Arribo,
                              format="%d/%m/%Y %H:%M:%S", errors="coerce")
    v["dur"] = (v.fin - v.ini).dt.total_seconds() / 60
    v = v.rename(columns={"Ciclo_Estacion_Retiro": "orig",
                          "Ciclo_EstacionArribo": "dest"})
    v["orig"] = v.orig.str.strip()
    v["dest"] = v.dest.str.strip()
    return v[["Bici", "orig", "dest", "ini", "dur"]]


def limpiar(v):
    n0 = len(v)
    v = v.dropna(subset=["ini", "dur", "orig", "dest"])
    v = v[(v.dur >= DURACION_MIN) & (v.dur <= DURACION_MAX)]
    # Quedarse con los meses que traen datos de verdad (algunos archivos traen
    # unas pocas fechas antiguas o erróneas), pero con TODOS esos meses
    meses = v.ini.dt.to_period("M").value_counts()
    meses = meses[meses >= MIN_FRAC_MES * meses.max()].index
    v = v[v.ini.dt.to_period("M").isin(meses)]
    print(f"  Limpieza: {n0:,} -> {len(v):,} viajes (meses {', '.join(str(m) for m in sorted(meses))}, "
          f"duración {DURACION_MIN}-{DURACION_MAX} min)")
    return v


# ---------------------------------------------------------------
# Códigos del área
# ---------------------------------------------------------------
def normalizar(c):
    """'027' -> '27';  '107-108' -> '107-108';  ' 001 ' -> '1'. Sirve para comparar códigos."""
    partes = [p.strip() for p in str(c).split("-")]
    return "-".join(str(int(p)) if p.isdigit() else p for p in partes)


def leer_area(ruta):
    a = pd.read_csv(ruta, dtype=str)
    if "code" not in a.columns:
        sys.exit(f"{ruta} no tiene la columna 'code' (los códigos de los viajes, p. ej. 026 o 107-108)")
    return set(a["code"].map(normalizar))


def codigos_area(todos_codigos, lista):
    """Códigos del archivo de viajes que pertenecen al área (comparación exacta del código)."""
    area = {c for c in todos_codigos if normalizar(c) in lista}
    faltan = sorted(lista - {normalizar(c) for c in area})
    return area, faltan


# ---------------------------------------------------------------
# Cálculo
# ---------------------------------------------------------------
def bloque(h):
    for nombre, horas in BLOQUES.items():
        if h in horas:
            return nombre
    return "?"


def main(rutas, ruta_area=ARCHIVO_AREA, ruta_info=None):
    if not os.path.isfile(ruta_area):
        sys.exit(f"No encontré {ruta_area}. Ponlo en esta carpeta o indícalo con --area archivo.csv")
    lista = leer_area(ruta_area)

    print("Leyendo viajes...")
    v = limpiar(leer_viajes(rutas))
    dias = v.ini.dt.normalize().nunique()

    todos = set(v.orig) | set(v.dest)
    area, faltan = codigos_area(todos, lista)
    print(f"\nCódigos del área en los viajes ({len(area)}): {', '.join(sorted(area))}")
    if faltan:
        print(f"  ! No aparecen en los viajes: {faltan}")

    v["o_in"] = v.orig.isin(area)
    v["d_in"] = v.dest.isin(area)
    v["bloque"] = v.ini.dt.hour.map(bloque)
    v["habil"] = v.ini.dt.dayofweek < 5

    internos = v[v.o_in & v.d_in]
    sal = v[v.o_in & ~v.d_in]      # área -> externa
    ent = v[~v.o_in & v.d_in]      # externa -> área
    frontera = len(sal) + len(ent)

    # Totales de cada estación externa (todos sus viajes, para la dependencia)
    tot_est = pd.concat([v.orig, v.dest]).value_counts()

    r = pd.DataFrame({
        "salidas_desde_area": sal.dest.value_counts(),
        "entradas_hacia_area": ent.orig.value_counts(),
    }).fillna(0).astype(int)
    r["total"] = r.sum(axis=1)
    r["neto_hacia_estacion"] = r.salidas_desde_area - r.entradas_hacia_area
    r["viajes_dia"] = r.total / dias
    r["peso_para_area"] = r.total / frontera
    r["dependencia"] = r.total / tot_est.reindex(r.index)
    r = r.sort_values("total", ascending=False)
    r["peso_acumulado"] = r.peso_para_area.cumsum()

    # Peso por bloque horario y tipo de día (ayuda a ver cuándo importa cada una)
    front = pd.concat([sal.assign(est=sal.dest), ent.assign(est=ent.orig)])
    por_bloque = (front.groupby(["est", "bloque"]).size().unstack(fill_value=0)
                  .reindex(columns=list(BLOQUES), fill_value=0))
    por_bloque.columns = [f"viajes_{c.split()[0].lower()}_{c.split()[1].lower()}"
                          for c in por_bloque.columns]
    r = r.join(por_bloque)
    r["pct_dias_habiles"] = (front[front.habil].groupby("est").size()
                             .reindex(r.index).fillna(0) / r.total)

    # Criterios de selección
    r["criterio_cobertura"] = (r.peso_acumulado - r.peso_para_area) < COBERTURA
    r["criterio_dependencia"] = (r.dependencia >= DEPENDENCIA_MIN) & (r.viajes_dia >= VIAJES_MIN_DIA)
    r["clave"] = r.criterio_cobertura | r.criterio_dependencia

    # Información opcional: nombre y distancia al centro del área
    if ruta_info:
        info = pd.read_csv(ruta_info, dtype=str)
        if "code" not in info.columns and "name" in info.columns:
            info["code"] = info["name"].str.extract(r"CE-(\S+)")[0]
        if {"code", "lat", "lon"} <= set(info.columns):
            info = info.dropna(subset=["code"])
            info["code"] = info.code.map(normalizar)
            info[["lat", "lon"]] = info[["lat", "lon"]].astype(float)
            info = info.drop_duplicates("code").set_index("code")
            r["_code"] = r.index.map(normalizar)
            cent = info.reindex(sorted(lista))[["lat", "lon"]].mean()
            r = r.join(info[[c for c in ("name", "lat", "lon") if c in info.columns]], on="_code").drop(columns="_code")
            r["dist_km_centro"] = 6371 * 2 * np.arcsin(np.sqrt(
                np.sin(np.radians(r.lat - cent.lat) / 2) ** 2 +
                np.cos(np.radians(cent.lat)) * np.cos(np.radians(r.lat)) *
                np.sin(np.radians(r.lon - cent.lon) / 2) ** 2))
        else:
            print("  ! --info ignorado: necesita columnas name (o code), lat, lon")

    r.index.name = "estacion"
    redondeo = {c: 3 for c in ("viajes_dia", "peso_para_area", "dependencia",
                                "peso_acumulado", "pct_dias_habiles", "dist_km_centro")}
    r.round(redondeo).to_csv("estaciones_relacionadas.csv")
    clave = r[r.clave]
    clave.round(redondeo).to_csv("estaciones_clave.csv")

    # Resumen
    total_area = len(internos) + frontera
    lineas = [
        f"Archivos: {', '.join(rutas)}",
        f"Días analizados: {dias}",
        f"Viajes que tocan el área: {total_area:,}  ({total_area / dias:.0f} por día)",
        f"  Internos (área -> área):   {len(internos):,}  ({len(internos) / total_area:.1%})",
        f"  Salen del área:            {len(sal):,}  ({len(sal) / total_area:.1%})",
        f"  Llegan al área:            {len(ent):,}  ({len(ent) / total_area:.1%})",
        f"Estaciones externas que intercambian viajes con el área: {len(r)}",
        f"Estaciones clave: {len(clave)}",
        f"  - cubren el {COBERTURA:.0%} del flujo de frontera: {int(r.criterio_cobertura.sum())}",
        f"  - dependen del área (>= {DEPENDENCIA_MIN:.0%} de sus viajes y >= {VIAJES_MIN_DIA} viaje/día): "
        f"{int(r.criterio_dependencia.sum())}",
        f"  Las estaciones clave reúnen el {clave.peso_para_area.sum():.1%} del flujo de frontera",
        "",
        "Top 20 estaciones relacionadas:",
        f"{'estación':>9} {'viajes/día':>10} {'sale→':>6} {'←entra':>7} "
        f"{'peso área':>9} {'acum.':>6} {'dependencia':>11}",
    ]
    for est, x in r.head(20).iterrows():
        lineas.append(f"{est:>9} {x.viajes_dia:>10.1f} {x.salidas_desde_area:>6} "
                      f"{x.entradas_hacia_area:>7} {x.peso_para_area:>9.1%} "
                      f"{x.peso_acumulado:>6.1%} {x.dependencia:>11.1%}")
    lineas += ["", "Estaciones que más dependen del área (dependencia, con >= 1 viaje/día):"]
    dep = r[r.viajes_dia >= VIAJES_MIN_DIA].sort_values("dependencia", ascending=False).head(10)
    for est, x in dep.iterrows():
        lineas.append(f"{est:>9}  {x.dependencia:.1%} de sus viajes  ({x.viajes_dia:.1f} viajes/día con el área)")

    texto = "\n".join(lineas)
    print("\n" + texto)
    with open("resumen_area.txt", "w", encoding="utf-8") as f:
        f.write(texto + "\n")
    print("\nArchivos generados: estaciones_relacionadas.csv, estaciones_clave.csv, resumen_area.txt")


def sacar_opcion(args, nombre):
    if nombre in args:
        i = args.index(nombre)
        valor = args[i + 1]
        return args[:i] + args[i + 2:], valor
    return args, None


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.strip() not in ("\\", "^", "`", "")]
    args, info = sacar_opcion(args, "--info")
    args, area = sacar_opcion(args, "--area")
    if not args:
        sys.exit(__doc__)
    main(args, area or ARCHIVO_AREA, info)
