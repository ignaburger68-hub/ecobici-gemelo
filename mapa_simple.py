"""
mapa_simple.py - Las 30 estaciones del gemelo (azul), el área de trabajo
(naranjo) y las estaciones relacionadas (verde) sobre una foto satelital o un
mapa de calles.

No necesita contextily: descarga el fondo directamente. Funciona en Python 3.7+.

Uso (en una sola línea):
    python -m pip install pandas matplotlib pillow
    python mapa_simple.py estaciones_seleccionadas.csv info_2026-11-07.csv --area-trabajo area_trabajo.txt --relacionadas estaciones_clave.csv

Argumentos:
    1. estaciones_seleccionadas.csv  las 30 estaciones del gemelo (en azul)
    2. info_AAAA-MM-DD.csv           coordenadas de todas las estaciones (del
                                     recolector: station_id, name, lat, lon).
                                     El código CE-xxx se saca del nombre.
    --area-trabajo archivo   (opcional) estaciones del área de trabajo, en naranjo
    --relacionadas archivo   (opcional) estaciones relacionadas, en verde
       Cada lista puede ser un .csv (columna "estacion" o "code", p. ej.
       estaciones_clave.csv) o un .txt con un código por línea (27, 107-108, 1...).
       Se puede usar una, las dos o ninguna.

Si una estación está en varias listas, se dibuja con un solo color, en este
orden de prioridad: azul (las 30) > naranjo (área de trabajo) > verde.

Salida: mapa_simple.png
(Si no hay internet, dibuja los puntos sin fondo.)
"""
import io
import math
import os
import sys

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

# ---------------- opciones ----------------
SATELITAL = False          # True: foto satelital (Esri) | False: mapa de calles (OpenStreetMap)
ZOOM_MAX = 16             # detalle máximo del fondo (se baja solo si el área es grande)
BALDOSAS_MAX = 80         # límite de baldosas a descargar (más = más lento)
MARGEN = 0.003            # margen alrededor de las estaciones, en grados
ETIQUETAS_AZULES = True   # escribir el código junto a las 30 estaciones
ETIQUETAS_NARANJAS = False  # escribir el código junto al área de trabajo (con muchas se ve cargado)
ETIQUETAS_VERDES = False  # escribir el código junto a las relacionadas

AZUL, NARANJO, VERDE = "#1f6fd1", "#ff8c1a", "#2ecc40"
URL_SAT = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
URL_OSM = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"


# ---------- códigos de estación ----------
def normalizar(c):
    """'027' -> '27';  '107-108' -> '107-108'. Sirve para comparar códigos escritos distinto."""
    partes = [p.strip() for p in str(c).split("-")]
    return "-".join(str(int(p)) if p.isdigit() else p for p in partes)


def leer_relacionadas(ruta):
    if ruta.lower().endswith(".csv"):
        df = pd.read_csv(ruta, dtype=str)
        col = next((c for c in ("estacion", "code", "codigo") if c in df.columns), df.columns[0])
        codigos = df[col]
    else:
        with open(ruta, encoding="utf-8") as f:
            codigos = f.read().replace(",", " ").split()
    return [normalizar(c) for c in codigos if str(c).strip()]


def leer_info(ruta):
    info = pd.read_csv(ruta, dtype={"station_id": str})
    if "code" not in info.columns:
        info["code"] = info["name"].str.extract(r"CE-(\S+)")[0]
    info = info.dropna(subset=["code"])
    info["code_n"] = info["code"].map(normalizar)
    return info.drop_duplicates("code_n").set_index("code_n")


# ---------- conversión entre coordenadas y "baldosas" del mapa ----------
def a_baldosa(lat, lon, z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y


def a_coord(x, y, z):
    n = 2 ** z
    lon = x / n * 360 - 180
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lat, lon


def elegir_zoom(lat_min, lat_max, lon_min, lon_max):
    """El mayor zoom (hasta ZOOM_MAX) que no pase de BALDOSAS_MAX baldosas."""
    for z in range(ZOOM_MAX, 10, -1):
        x0, y0 = a_baldosa(lat_max, lon_min, z)
        x1, y1 = a_baldosa(lat_min, lon_max, z)
        if (int(x1) - int(x0) + 1) * (int(y1) - int(y0) + 1) <= BALDOSAS_MAX:
            return z
    return 11


def descargar_fondo(lat_min, lat_max, lon_min, lon_max, z):
    """Descarga las baldosas que cubren la zona y las une en una sola imagen."""
    import urllib.request
    from PIL import Image

    x0, y0 = a_baldosa(lat_max, lon_min, z)   # esquina superior izquierda
    x1, y1 = a_baldosa(lat_min, lon_max, z)   # esquina inferior derecha
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    url = URL_SAT if SATELITAL else URL_OSM
    cabecera = {"User-Agent": "proyecto-simulacion-ecobici/1.0"}
    img = Image.new("RGB", ((x1 - x0 + 1) * 256, (y1 - y0 + 1) * 256))
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            pedido = urllib.request.Request(url.format(z=z, x=x, y=y), headers=cabecera)
            with urllib.request.urlopen(pedido, timeout=20) as r:
                datos = r.read()
            img.paste(Image.open(io.BytesIO(datos)).convert("RGB"),
                      ((x - x0) * 256, (y - y0) * 256))

    lat_sup, lon_izq = a_coord(x0, y0, z)
    lat_inf, lon_der = a_coord(x1 + 1, y1 + 1, z)
    return img, [lon_izq, lon_der, lat_inf, lat_sup]


def etiquetar(ax, puntos, color_texto, color_borde):
    for _, r in puntos.iterrows():
        ax.annotate(r["code"], (r["lon"], r["lat"]), xytext=(5, 5),
                    textcoords="offset points", fontsize=7, fontweight="bold",
                    color=color_texto, zorder=6,
                    path_effects=[pe.withStroke(linewidth=2.5, foreground=color_borde)])


# ---------------- dibujo ----------------
def cargar_lista(ruta, info, ya_dibujadas, nombre):
    """Coordenadas de los códigos de la lista que no estén ya en una categoría de mayor prioridad."""
    codigos = list(dict.fromkeys(leer_relacionadas(ruta)))
    repetidas = [c for c in codigos if c in ya_dibujadas]
    nuevas = [c for c in codigos if c not in ya_dibujadas]
    faltan = [c for c in nuevas if c not in info.index]
    if repetidas:
        print(f"Aviso ({nombre}): {len(repetidas)} códigos ya están en una categoría de mayor "
              f"prioridad y no se repiten: {', '.join(repetidas)}")
    if faltan:
        print(f"Aviso ({nombre}): {len(faltan)} códigos sin coordenadas en el archivo info: {', '.join(faltan)}")
    return info.reindex([c for c in nuevas if c in info.index])[["code", "lat", "lon"]]


def main(ruta_sel, ruta_info=None, ruta_trabajo=None, ruta_rel=None):
    for r in (ruta_sel, ruta_info, ruta_trabajo, ruta_rel):
        if r and not os.path.isfile(r):
            sys.exit(f"No encontré el archivo {r} (carpeta actual: {os.getcwd()})")
    if (ruta_trabajo or ruta_rel) and not ruta_info:
        sys.exit("Para dibujar el área de trabajo o las relacionadas hace falta el archivo info con las coordenadas")

    sel = pd.read_csv(ruta_sel, dtype={"station_id": str, "code": str})
    sel["code_n"] = sel["code"].map(normalizar)
    vacio = pd.DataFrame(columns=["code", "lat", "lon"])
    trabajo, rel = vacio, vacio
    if ruta_info:
        info = leer_info(ruta_info)
        dibujadas = set(sel["code_n"])
        if ruta_trabajo:
            trabajo = cargar_lista(ruta_trabajo, info, dibujadas, "área de trabajo")
            dibujadas |= set(trabajo.index)
        if ruta_rel:
            rel = cargar_lista(ruta_rel, info, dibujadas, "relacionadas")

    todas = pd.concat([sel[["lat", "lon"]], trabajo[["lat", "lon"]], rel[["lat", "lon"]]]).astype(float)
    lat_min, lat_max = todas["lat"].min() - MARGEN, todas["lat"].max() + MARGEN
    lon_min, lon_max = todas["lon"].min() - MARGEN, todas["lon"].max() + MARGEN

    fig, ax = plt.subplots(figsize=(10, 10))
    try:
        z = elegir_zoom(lat_min, lat_max, lon_min, lon_max)
        img, extension = descargar_fondo(lat_min, lat_max, lon_min, lon_max, z)
        ax.imshow(img, extent=extension, zorder=1)
    except Exception as e:
        print("Sin fondo de mapa:", e)

    borde = "white" if SATELITAL else "black"
    texto, contorno = ("white", "black") if SATELITAL else ("black", "white")
    capas = [  # (puntos, color, tamaño, etiquetas, nombre en la leyenda)
        (rel, VERDE, 40, ETIQUETAS_VERDES, "Estaciones relacionadas"),
        (trabajo, NARANJO, 50, ETIQUETAS_NARANJAS, "Área de trabajo"),
        (sel, AZUL, 90, ETIQUETAS_AZULES, "Estaciones del gemelo"),
    ]
    leyenda = []
    for orden, (puntos, color, tam, etiquetas, nombre) in enumerate(capas):
        if not len(puntos):
            continue
        ax.scatter(puntos["lon"].astype(float), puntos["lat"].astype(float), s=tam, c=color,
                   edgecolor=borde, linewidth=0.8 if tam < 90 else 1.2, zorder=3 + orden)
        if etiquetas:
            etiquetar(ax, puntos, texto, contorno)
        leyenda.insert(0, Line2D([], [], marker="o", ls="", ms=math.sqrt(tam), mfc=color, mec=borde,
                                 label=f"{nombre} ({len(puntos)})"))
    ax.legend(handles=leyenda, loc="upper left", fontsize=9, framealpha=0.9)

    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect(1 / math.cos(math.radians(todas["lat"].mean())))
    ax.set_title("Estaciones Ecobici del gemelo digital" if len(leyenda) > 1
                 else "Estaciones Ecobici seleccionadas")
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    fuente = "Imagen satelital: Esri World Imagery" if SATELITAL else "© OpenStreetMap"
    ax.text(0.99, 0.01, fuente, transform=ax.transAxes, ha="right", va="bottom",
            fontsize=7, color="white" if SATELITAL else "black")
    plt.tight_layout()
    plt.savefig("mapa_simple.png", dpi=150)
    print(f"Listo: mapa_simple.png  ({len(sel)} en azul, {len(trabajo)} en naranjo, {len(rel)} en verde)")


def sacar_opcion(args, nombre):
    if nombre in args:
        i = args.index(nombre)
        if i + 1 >= len(args):
            sys.exit(f"Falta el archivo después de {nombre}")
        return args[:i] + args[i + 2:], args[i + 1]
    return args, None


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.strip() not in ("\\", "^", "`", "")]
    args, trabajo = sacar_opcion(args, "--area-trabajo")
    args, rel = sacar_opcion(args, "--relacionadas")
    if len(args) == 3 and rel is None:   # forma antigua: el tercer archivo son las relacionadas
        args, rel = args[:2], args[2]
    if not 1 <= len(args) <= 2:
        sys.exit(__doc__)
    main(args[0], args[1] if len(args) > 1 else None, trabajo, rel)
