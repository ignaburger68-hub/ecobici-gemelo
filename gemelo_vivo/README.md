# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 16:37 (hora de Ciudad de México).

## Último pronóstico: 24/11 16:37 a 17:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.7 °C** · lluvia 1.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.63** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 003 Reforma - Insurgentes | 0 / 27 | 1.00 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.97 | 0.00 | 2-11 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.96 | 7-14 |
| 115 Roma-Dinamarca | 1 / 26 | 0.93 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 15 | 0.90 | 0.01 | 0-8 |
| 114 Lucerna-Abraham González | 20 / 21 | 0.00 | 0.87 | 15-21 |
| 555 Ribera de San Cosme - Insurg | 1 / 29 | 0.86 | 0.00 | 1-11 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.76 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.73 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 114 (20/21) a 003 (0/27)
2. Llevar **16 bicis** de 098 (26/29) a 115 (1/26)
3. Llevar **11 bicis** de 116 (15/23) a 555 (1/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

552 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.083 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
