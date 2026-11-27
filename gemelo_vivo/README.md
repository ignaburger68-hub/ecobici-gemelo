# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 10:23 (hora de Ciudad de México).

## Último pronóstico: 27/11 10:22 a 11:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.4 °C** · lluvia 0.8 mm/h · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.66** y las **devoluciones por 0.74** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 14 / 14 | 0.00 | 0.98 | 9-14 |
| 118 Liverpool-Dinamarca | 17 / 19 | 0.00 | 0.96 | 17-19 |
| 107-108 Tolsa-Balderas | 0 / 27 | 0.91 | 0.00 | 2-10 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.82 | 10-15 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.81 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.77 | 0.00 | 0-4 |
| 116 Londres-Roma | 1 / 21 | 0.75 | 0.00 | 1-10 |
| 115 Roma-Dinamarca | 21 / 23 | 0.00 | 0.69 | 17-23 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (17/19) a 086 (0/14)
2. Llevar **8 bicis** de 012 (14/14) a 256 (1/21)
3. Llevar **8 bicis** de 113 (14/15) a 255 (1/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

740 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.244 | 0.081 |
| Persistencia | 0.251 | 0.061 |
| Persistencia 0/1 | 0.251 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
