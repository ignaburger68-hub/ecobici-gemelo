# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 19:52 (hora de Ciudad de México).

## Último pronóstico: 27/11 19:52 a 20:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.1 °C** · lluvia 1.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.56** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.99 | 21-23 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 14 / 15 | 0.00 | 0.74 | 12-15 |
| 117 Londres-Nápoles | 2 / 28 | 0.36 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 24 | 0.31 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 2 / 16 | 0.28 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 2 / 25 | 0.27 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 2 / 14 | 0.19 | 0.00 | 1-5 |
| 119 Turín-Abraham González | 23 / 26 | 0.00 | 0.17 | 21-26 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 114 (23/23) a 012 (0/11)
2. Llevar **7 bicis** de 086 (14/15) a 117 (2/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

780 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.239 | 0.082 |
| Persistencia | 0.243 | 0.060 |
| Persistencia 0/1 | 0.243 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
