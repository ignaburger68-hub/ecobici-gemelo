# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 16:50 (hora de Ciudad de México).

## Último pronóstico: 22/11 16:50 a 17:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.61** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 21 | 0.98 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.80 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 25 | 0.78 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 26 / 27 | 0.00 | 0.69 | 21-27 |
| 555 Ribera de San Cosme - Insurg | 2 / 32 | 0.69 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.65 | 6-11 |
| 113 General Prim-Versalles | 2 / 14 | 0.57 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 26 | 0.00 | 0.52 | 21-26 |
| 119 Turín-Abraham González | 2 / 27 | 0.48 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 4 / 35 | 0.34 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 041 (26/27) a 555 (2/32)
2. Llevar **10 bicis** de 259 (24/26) a 256 (1/22)
3. Llevar **5 bicis** de 026 (10/11) a 115 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

411 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
