# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 16:51 (hora de Ciudad de México).

## Último pronóstico: 24/11 16:51 a 17:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.7 °C** · lluvia 1.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.55** y las **devoluciones por 0.62** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-7 |
| 115 Roma-Dinamarca | 0 / 26 | 0.98 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 29 | 0.98 | 0.00 | 3-15 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.87 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.78 | 0.00 | 0-7 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.72 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 18 / 19 | 0.00 | 0.68 | 11-19 |
| 098 Emilio Dondé-Av. Balderas | 26 / 29 | 0.00 | 0.66 | 25-29 |
| 113 General Prim-Versalles | 13 / 14 | 0.01 | 0.64 | 6-14 |
| 107-108 Tolsa-Balderas | 2 / 55 | 0.63 | 0.00 | 3-14 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 098 (26/29) a 115 (0/26)
2. Llevar **12 bicis** de 114 (19/21) a 041 (0/31)
3. Llevar **9 bicis** de 112 (18/19) a 555 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

553 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
