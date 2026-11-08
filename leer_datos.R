# =====================================================================
# Une todas las lecturas guardadas por el recolector en una sola tabla.
# Sirve para los datos de la nube (.csv.gz por ejecución) y para los del
# computador (.csv por día).
#
# Uso, desde la carpeta del repositorio:
#   source("leer_datos.R")
#   s <- leer_status()                       # todas las lecturas
#   s <- leer_status(desde = "2026-11-10")   # solo desde una fecha (UTC)
#   info <- leer_info()                      # estaciones (última versión)
# =====================================================================

leer_status <- function(carpeta = "datos/status", desde = NULL) {
  archivos <- list.files(carpeta, pattern = "\\.csv(\\.gz)?$",
                         recursive = TRUE, full.names = TRUE)
  if (!is.null(desde)) {
    fechas   <- regmatches(basename(archivos), regexpr("\\d{4}-\\d{2}-\\d{2}", basename(archivos)))
    archivos <- archivos[as.Date(fechas) >= as.Date(desde)]
  }
  if (length(archivos) == 0) stop("No hay archivos en ", carpeta)
  partes <- lapply(archivos, function(a)
    read.csv(a, colClasses = c(station_id = "character"), encoding = "UTF-8"))
  s <- do.call(rbind, partes)
  s$lectura_utc <- as.POSIXct(s$lectura_utc, tz = "UTC")
  s$hora_cdmx   <- format(s$lectura_utc, tz = "America/Mexico_City", usetz = FALSE)
  s <- s[!duplicated(s[, c("lectura_utc", "station_id")]), ]
  s[order(s$station_id, s$lectura_utc), ]
}

leer_info <- function(carpeta = "datos/info") {
  archivos <- sort(list.files(carpeta, pattern = "\\.csv$", full.names = TRUE))
  if (length(archivos) == 0) stop("No hay archivos en ", carpeta)
  read.csv(tail(archivos, 1), colClasses = c(station_id = "character"), encoding = "UTF-8")
}

# Resumen rápido para revisar que la recolección va bien
revisar <- function(s) {
  lecturas <- sort(unique(s$lectura_utc))
  saltos   <- as.numeric(diff(lecturas), units = "mins")
  cat("Lecturas:", length(lecturas), " desde", format(min(lecturas)),
      "hasta", format(max(lecturas)), "UTC\n")
  cat("Estaciones:", length(unique(s$station_id)), "\n")
  cat("Huecos de más de 5 minutos:", sum(saltos > 5), "\n")
  if (any(saltos > 5)) {
    i <- which(saltos > 5)
    print(data.frame(desde = lecturas[i], hasta = lecturas[i + 1],
                     minutos = round(saltos[i])))
  }
}
