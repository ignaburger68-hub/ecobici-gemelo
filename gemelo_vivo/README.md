# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 11:06 (hora de Ciudad de México).

## Último pronóstico: 26/11 11:06 a 12:06

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
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 28 / 28 | 0.00 | 0.99 | 23-28 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.95 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.89 | 0.95 | 2-2 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.91 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 12 | 0.88 | 0.08 | 3-11 |
| 026 Reforma - Versalles | 1 / 11 | 0.85 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.82 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 117 (28/28) a 012 (1/15)
2. Llevar **9 bicis** de 260 (19/21) a 256 (1/22)
3. Llevar **8 bicis** de 118 (14/19) a 259 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

671 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
