# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 13:56 (hora de Ciudad de México).

## Último pronóstico: 26/11 13:56 a 14:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

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
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 34 | 0.98 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.98 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.95 | 9-18 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.93 | 0.61 | 2-5 |
| 029 Reforma - Bucareli | 0 / 9 | 0.92 | 0.47 | 4-9 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.90 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.85 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 9 | 0.84 | 0.01 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (12/14) a 041 (0/32)
2. Llevar **8 bicis** de 118 (19/19) a 256 (1/23)
3. Llevar **11 bicis** de 260 (19/21) a 107-108 (3/55)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

683 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
