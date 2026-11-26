# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 11:20 (hora de Ciudad de México).

## Último pronóstico: 26/11 11:20 a 12:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.92 | 0.99 | 1-1 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.99 | 24-27 |
| 029 Reforma - Bucareli | 0 / 11 | 0.89 | 0.30 | 4-11 |
| 041 Reforma - Av. de la Repúblic | 2 / 32 | 0.85 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 3 / 15 | 0.76 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.74 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 12 | 0.71 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 55 | 0.66 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (27/27) a 259 (0/26)
2. Llevar **12 bicis** de 260 (19/21) a 041 (2/32)
3. Llevar **8 bicis** de 115 (21/23) a 012 (3/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

672 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.244 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
