# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 14:53 (hora de Ciudad de México).

## Último pronóstico: 26/11 14:53 a 15:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.9 °C** · lluvia 0.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 33 | 0.99 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.94 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 9 | 0.93 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 12 | 0.91 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.90 | 0.46 | 2-6 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.89 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.89 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 7 | 0.86 | 0.60 | 3-7 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 117 (27/28) a 010 (0/25)
2. Llevar **10 bicis** de 260 (19/21) a 555 (0/33)
3. Llevar **10 bicis** de 114 (19/22) a 041 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

687 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
