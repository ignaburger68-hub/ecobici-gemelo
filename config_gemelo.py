"""
config_gemelo.py - Parámetros del gemelo digital Ecobici
Proyecto Simulación · Tema 3 · Ignacio Chandia y Francisco Correa

Todos los parámetros del modelo están aquí. Para cambiar algo, cámbialo en
este archivo y vuelve a correr; no hace falta tocar el resto del código.
Los marcados como SUPUESTO no tienen todavía un dato real que los respalde.
"""

# ---------------------------------------------------------------------
# Archivos y carpetas (rutas relativas a la carpeta donde se corre)
# ---------------------------------------------------------------------
ZONA = "America/Mexico_City"
ARCHIVO_ESTACIONES = "estaciones_seleccionadas.csv"    # code, station_id, name, lat, lon, capacity, perfil
CARPETA_STATUS = "datos/status"                        # lecturas del recolector (.csv y .csv.gz)
VIAJES = ["public_data_web_*.csv"]                     # archivos, carpetas o comodines de viajes
ARCHIVO_CLIMA = "datos/clima/clima_horario.csv"        # de clima_ecobici.py historico
ARCHIVO_FACTORES_CLIMA = "resultados_clima/factores_clima_gemelo.csv"   # de clima_demanda.py (opcional)
ARCHIVO_KAPPA = "kappa.csv"                            # opcional: columnas code, kappa
CARPETA_CACHE = "cache_gemelo"
CARPETA_RESULTADOS = "resultados_gemelo"
ARCHIVO_PARAMETROS = "resultados_gemelo/parametros_elegidos.json"     # lo escribe "ajuste"
ARCHIVO_PERFIL_BASE = "perfil_base_15min.csv"          # lo escribe "preparar"; se usa si no hay viajes
URL_GBFS = "https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json"

# ---------------------------------------------------------------------
# Gemelo en vivo (comando "ciclo", pensado para correr solo en GitHub Actions)
# ---------------------------------------------------------------------
CARPETA_VIVO = "gemelo_vivo"     # registro de pronósticos, evaluaciones y página con el último pronóstico
FEED_DIAS_VIVO = 21              # en vivo sólo se leen las lecturas de los últimos N días (más rápido)
HORA_INICIO_VIVO = "06:00"       # fuera de este horario el ciclo sólo evalúa, no pronostica
HORA_FIN_VIVO = "23:00"

# ---------------------------------------------------------------------
# Calendario
# ---------------------------------------------------------------------
FESTIVOS = ["2026-09-16", "2026-11-02", "2026-11-16"]   # cuentan como fin de semana
HORAS_SERVICIO = range(5, 24)                         # 05:00 a 23:59 (el sistema cierra 00:30-05:00)

# ---------------------------------------------------------------------
# Viajes históricos (perfil base)
# ---------------------------------------------------------------------
MESES_HISTORIA = 3          # se usan los últimos N meses completos publicados antes del pronóstico
MIN_DIAS_MES = 20           # un mes cuenta como "completo" si tiene al menos estos días válidos
MIN_FRAC_DIA = 0.10         # días con menos del 10 % de los viajes de un día típico se descartan
S_MODO = "perfil"           # reparto dentro de la hora: "global", "perfil" o "estacion"
SOLO_SECO = True            # perfil base sólo con horas secas (el clima se aplica después)
UMBRAL_LLUVIA = 0.1         # mm en la hora
UMBRAL_LLUVIA_PREVIA = 0.5  # mm en las 3 h previas

# ---------------------------------------------------------------------
# Feed GBFS
# ---------------------------------------------------------------------
INICIO_FEED = "2026-11-09"  # lecturas limpias desde este día (hora local)
MAX_RELLENO_MIN = 5         # minutos sin lectura que se rellenan con la lectura anterior
MAX_HUECO_MIN = 60          # si una estación no actualiza su reporte por más de esto, ese tramo queda
                            # "sin dato". Con los datos reales (diagnóstico del 16/11) la mediana entre
                            # reportes es 2 min, pero el 10,8 % supera los 10 min y el 1 % los 59 min:
                            # las estaciones tranquilas reportan poco. Con 60 sólo se descarta ~1 %.
UMBRAL_CAMION = 4           # salto de más de 4 bicis entre reportes = camión del operador
MIN_COBERTURA_HORA = 45     # minutos con dato (de 60) para evaluar un pronóstico
MIN_COBERTURA_DIA = 0.5     # fracción de minutos 05-24 con dato para usar un día en la ventana

# ---------------------------------------------------------------------
# Tasas (Función 1 del planteamiento)
# ---------------------------------------------------------------------
W_DIAS = 7                  # días hábiles de la ventana móvil (lo cambia "ajuste")
M_CONFIANZA = 10            # m: eventos "equivalentes" que pesa el perfil base (lo cambia "ajuste")
A_FACTOR = 20               # suavizado del factor común del día
F_MIN, F_MAX = 0.4, 2.5     # límites del factor común del día
KAPPA = 1.05                # SUPUESTO: corrección por retiros/devoluciones del mismo minuto
PHI_POR_FRANJA = {          # SUPUESTO: sobredispersión entre días (varianza del multiplicador Gamma)
    (5, 7): 0.15,
    (7, 10): 0.10,
    (10, 17): 0.10,
    (17, 20): 0.10,
    (20, 24): 0.15,
}
USAR_PHI = True             # lo cambia "ajuste"

# ---------------------------------------------------------------------
# Simulación
# ---------------------------------------------------------------------
R = 1000                    # réplicas por pronóstico
R_AJUSTE = 500              # réplicas en el ajuste (más rápido)
R_PLANES = 1000             # réplicas para comparar planes
SEMILLA = 2026
HORIZONTE_MIN = 60
PRIMER_T0 = "06:00"
ULTIMO_T0 = "22:45"
PASO_T0_MIN = 15

# ---------------------------------------------------------------------
# Rebalanceo (Función 4)
# ---------------------------------------------------------------------
Q_CAMION = 20               # SUPUESTO: capacidad del camión (bicis)
MAX_TRASLADOS = 3
MEJORA_MIN = 0.5            # no se mueve el camión por menos de 0,5 usuarios atendidos
UMBRAL_ALTO = 0.8           # regla umbral: origen con ocupación > 80 %
UMBRAL_BAJO = 0.2           # regla umbral: destino con ocupación < 20 %
OCUPACION_OBJETIVO = 0.5    # regla umbral: ambas quedan cerca del 50 %
VEL_KMH = 15                # sensibilidad con tiempos de viaje
FACTOR_RUTA = 1.3           # distancia por calles / distancia en línea recta
MIN_CARGA = 5
MIN_DESCARGA = 5

# ---------------------------------------------------------------------
# Ajuste y evaluación
# ---------------------------------------------------------------------
GRILLA_W = [3, 7]
GRILLA_M = [5, 10, 20, 40]
GRILLA_PHI = [False, True]
CORTES_PERSISTENCIA = [1, 2, 3, 5, 8]   # grupos de bicis (o anclajes): 0, 1, 2, 3-4, 5-7, 8+
N_BOOTSTRAP = 2000
