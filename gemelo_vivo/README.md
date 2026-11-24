# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 17:06 (hora de Ciudad de México).

## Último pronóstico: 24/11 17:06 a 18:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.7 °C** · lluvia 1.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.54** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 21 | 0.99 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.89 | 0.00 | 0-8 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.89 | 0.00 | 0-8 |
| 260 Av. Juárez-Balderas | 15 / 19 | 0.00 | 0.89 | 16-19 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.88 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.86 | 0.00 | 2-15 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.75 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 26 / 29 | 0.00 | 0.74 | 26-29 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.72 | 0.00 | 1-8 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 23 | 0.49 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (15/19) a 010 (0/21)
2. Llevar **14 bicis** de 098 (26/29) a 003 (1/27)
3. Llevar **9 bicis** de 114 (18/21) a 041 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

554 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
