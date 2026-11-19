"""
Selección de 30 estaciones Ecobici para el gemelo digital.

Uso:
    python seleccionar_estaciones.py info_2026-11-07.csv public_data_web_2026-08.csv public_data_web_2026-09.csv public_data_web_2026-10.csv

Entradas:
    - Archivo de información de estaciones (station_id, name, lat, lon, capacity).
    - Uno o más CSV mensuales de viajes históricos de Ecobici.

Salidas (en la carpeta actual):
    - metricas_todas_estaciones.csv : demanda y desbalance de cada estación
    - grupos_candidatos.csv         : evaluación de cada grupo posible de 30 estaciones
    - estaciones_seleccionadas.csv  : las 30 estaciones elegidas
    - mapa_estaciones.png           : mapa del grupo elegido

Requisitos: pandas, numpy, matplotlib
"""

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Parámetros
# ---------------------------------------------------------------
N_ESTACIONES = 30          # tamaño del grupo
RADIO_MAX_KM = 1.3         # distancia máxima desde la estación central
CAPACIDAD_MIN = 10         # descartar estaciones muy pequeñas
UMBRAL_PERFIL = 0.20       # |neto mañana| / capacidad para clasificar perfil
MEZCLA_MIN = 10            # mínimo de estaciones que se llenan y que se vacían
HORAS_AM = (7, 9)          # bloque mañana: 7:00 a 9:59
HORAS_PM = (17, 19)        # bloque tarde: 17:00 a 19:59


# ---------------------------------------------------------------
# 1. Lectura de datos
# ---------------------------------------------------------------
def leer_info(ruta):
    info = pd.read_csv(ruta, dtype={"station_id": str})
    # Los viajes usan el código "CE-xxx" del nombre, no el station_id del feed
    info["code"] = info["name"].str.extract(r"CE-(\S+)")[0]
    return info


def leer_viajes(rutas):
    cols = ["Ciclo_Estacion_Retiro", "Fecha_Retiro", "Hora_Retiro",
            "Ciclo_EstacionArribo", "Fecha_Arribo", "Hora_Arribo"]
    df = pd.concat([pd.read_csv(r, dtype=str, usecols=cols) for r in rutas],
                   ignore_index=True)

    def eventos(est, fecha, hora):
        t = pd.to_datetime(df[fecha] + " " + df[hora],
                           format="%d/%m/%Y %H:%M:%S", errors="coerce")
        e = pd.DataFrame({"code": df[est], "t": t}).dropna()
        e["habil"] = e["t"].dt.dayofweek < 5
        e["hora"] = e["t"].dt.hour
        return e

    retiros = eventos("Ciclo_Estacion_Retiro", "Fecha_Retiro", "Hora_Retiro")
    devol = eventos("Ciclo_EstacionArribo", "Fecha_Arribo", "Hora_Arribo")

    # Quedarse con los meses principales (descarta viajes que empezaron el mes anterior)
    meses = retiros["t"].dt.to_period("M").value_counts()
    meses = meses[meses > 0.05 * meses.max()].index
    retiros = retiros[retiros["t"].dt.to_period("M").isin(meses)]
    devol = devol[devol["t"].dt.to_period("M").isin(meses)]
    return df, retiros, devol


# ---------------------------------------------------------------
# 2. Métricas por estación
# ---------------------------------------------------------------
def conteos(e, nombre):
    habil = e[e["habil"]]
    am = habil[habil["hora"].between(*HORAS_AM)]
    pm = habil[habil["hora"].between(*HORAS_PM)]
    return pd.concat([
        e.groupby("code").size().rename(nombre),
        am.groupby("code").size().rename(nombre + "_am"),
        pm.groupby("code").size().rename(nombre + "_pm"),
    ], axis=1)


def metricas(info, retiros, devol):
    n_dias = retiros["t"].dt.date.nunique()
    n_habiles = retiros.loc[retiros["habil"], "t"].dt.date.nunique()

    s = (info.set_index("code")
         .join(conteos(retiros, "ret"))
         .join(conteos(devol, "dev"))
         .fillna(0))

    s["demanda_dia"] = (s["ret"] + s["dev"]) / n_dias
    # Neto = devoluciones - retiros por día hábil (>0: se llena, <0: se vacía)
    s["neto_am"] = (s["dev_am"] - s["ret_am"]) / n_habiles
    s["neto_pm"] = (s["dev_pm"] - s["ret_pm"]) / n_habiles
    s["neto_am_rel"] = s["neto_am"] / s["capacity"]

    s["perfil"] = np.select(
        [s["neto_am_rel"] > UMBRAL_PERFIL, s["neto_am_rel"] < -UMBRAL_PERFIL],
        ["Se llena en la mañana", "Se vacía en la mañana"],
        default="Equilibrada")

    print(f"Días analizados: {n_dias} ({n_habiles} hábiles)")
    return s


# ---------------------------------------------------------------
# 3. Búsqueda del grupo de 30 estaciones
# ---------------------------------------------------------------
def distancias_km(lat, lon):
    lat, lon = np.radians(lat), np.radians(lon)
    dlat = lat[:, None] - lat
    dlon = lon[:, None] - lon
    a = (np.sin(dlat / 2) ** 2
         + np.cos(lat[:, None]) * np.cos(lat) * np.sin(dlon / 2) ** 2)
    return 2 * 6371 * np.arcsin(np.sqrt(a))


def buscar_grupos(s):
    """Para cada estación, arma el grupo con ella y sus 29 vecinas más cercanas."""
    s = s[(s["capacity"] >= CAPACIDAD_MIN) & (s["ret"] > 0)]
    D = distancias_km(s["lat"].values, s["lon"].values)
    perfil = s["perfil"].values

    filas = []
    for i in range(len(s)):
        idx = np.argsort(D[i])[:N_ESTACIONES]
        llenas = (perfil[idx] == "Se llena en la mañana").sum()
        vacias = (perfil[idx] == "Se vacía en la mañana").sum()
        filas.append({
            "code_central": s.index[i],
            "nombre_central": s["name"].iloc[i],
            "radio_km": D[i, idx].max(),
            "demanda_dia": s["demanda_dia"].iloc[idx].sum(),
            "n_se_llenan": llenas,
            "n_se_vacian": vacias,
            # mezcla: cuántos pares lleno/vacío puede emparejar el camión
            "mezcla": min(llenas, vacias),
        })
    grupos = pd.DataFrame(filas)
    return s, D, grupos


def elegir_grupo(s, D, grupos):
    # Criterio: entre los grupos compactos que tienen al menos MEZCLA_MIN
    # estaciones que se llenan y MEZCLA_MIN que se vacían, el de mayor demanda
    candidatos = grupos[(grupos["radio_km"] <= RADIO_MAX_KM)
                        & (grupos["mezcla"] >= MEZCLA_MIN)]
    mejor = candidatos.sort_values("demanda_dia", ascending=False).iloc[0]
    i = list(s.index).index(mejor["code_central"])
    idx = np.argsort(D[i])[:N_ESTACIONES]
    sel = s.iloc[idx].copy()
    sel["dist_central_km"] = D[i, idx]
    return mejor, sel


# ---------------------------------------------------------------
# 4. Resultados
# ---------------------------------------------------------------
def fraccion_viajes_internos(df, codigos):
    sal = df[df["Ciclo_Estacion_Retiro"].isin(codigos)]
    return sal["Ciclo_EstacionArribo"].isin(codigos).mean()


def dibujar_mapa(s_todas, sel, ruta="mapa_estaciones.png"):
    colores = {"Se llena en la mañana": "#c0392b",
               "Se vacía en la mañana": "#2471a3",
               "Equilibrada": "#7f8c8d"}
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.scatter(s_todas["lon"], s_todas["lat"], s=8, c="#cccccc",
               label="Otras estaciones")
    for perfil, g in sel.groupby("perfil"):
        ax.scatter(g["lon"], g["lat"], s=g["demanda_dia"] * 0.6,
                   c=colores[perfil], alpha=0.8, edgecolor="k", lw=0.5,
                   label=f"{perfil} ({len(g)})")
    for _, r in sel.iterrows():
        ax.annotate(r["station_id"], (r["lon"], r["lat"]), fontsize=7,
                    xytext=(4, 4), textcoords="offset points")
    ax.scatter(sel["lon"].mean(), sel["lat"].mean(), marker="*", s=250,
               c="gold", edgecolor="k", label="Centroide (clima)")
    m = 0.008
    ax.set_xlim(sel["lon"].min() - m, sel["lon"].max() + m)
    ax.set_ylim(sel["lat"].min() - m, sel["lat"].max() + m)
    ax.set_aspect(1 / np.cos(np.radians(sel["lat"].mean())))
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.set_title("Estaciones seleccionadas\n"
                 "(tamaño = viajes por día; etiqueta = station_id del feed GBFS)")
    ax.legend(loc="lower left", fontsize=8)
    plt.tight_layout()
    plt.savefig(ruta, dpi=150)


def main(ruta_info, rutas_viajes):
    info = leer_info(ruta_info)
    df, retiros, devol = leer_viajes(rutas_viajes)
    print(f"Viajes leídos: {len(df):,}")

    s = metricas(info, retiros, devol)
    s.to_csv("metricas_todas_estaciones.csv")

    s_filtrado, D, grupos = buscar_grupos(s)
    grupos.sort_values("demanda_dia", ascending=False).to_csv(
        "grupos_candidatos.csv", index=False)

    mejor, sel = elegir_grupo(s_filtrado, D, grupos)

    cols = ["station_id", "name", "lat", "lon", "capacity", "demanda_dia",
            "neto_am", "neto_pm", "perfil", "dist_central_km"]
    salida = sel.reset_index()[["code"] + cols].round(
        {"demanda_dia": 1, "neto_am": 1, "neto_pm": 1, "dist_central_km": 2})
    salida.to_csv("estaciones_seleccionadas.csv", index=False)
    dibujar_mapa(s_filtrado, sel)

    # Resumen
    max_dem = grupos.loc[grupos["radio_km"] <= RADIO_MAX_KM, "demanda_dia"].max()
    print("\n=== Grupo seleccionado ===")
    print(f"Estación central: {mejor['nombre_central']}")
    print(f"Radio: {mejor['radio_km']:.2f} km")
    print(f"Demanda: {mejor['demanda_dia']:.0f} viajes/día "
          f"({mejor['demanda_dia'] / s['demanda_dia'].sum():.1%} del sistema; "
          f"el grupo de mayor demanda tiene {max_dem:.0f})")
    print(f"Perfiles: {mejor['n_se_llenan']} se llenan, "
          f"{mejor['n_se_vacian']} se vacían en la mañana")
    print(f"Capacidad total: {sel['capacity'].sum():.0f} anclajes")
    print(f"Centroide (para el clima): lat {sel['lat'].mean():.5f}, "
          f"lon {sel['lon'].mean():.5f}")
    print(f"Viajes que salen del grupo y terminan dentro: "
          f"{fraccion_viajes_internos(df, set(sel.index)):.1%}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2:])
