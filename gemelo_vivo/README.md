# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 21:45 (hora de Ciudad de México).

## Último pronóstico: 27/11 21:45 a 22:45

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**7.9 °C** · lluvia 2.5 mm/h · viento 8 km/h · día hábil

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
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.98 | 13-16 |
| 117 Londres-Nápoles | 1 / 28 | 0.63 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.46 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 14 | 0.45 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.44 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 21 / 23 | 0.00 | 0.44 | 19-23 |
| 010 Reforma - Ramírez | 2 / 27 | 0.30 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 17 | 0.11 | 0.00 | 1-4 |
| 107-108 Tolsa-Balderas | 48 / 56 | 0.00 | 0.06 | 48-54 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 086 (16/16) a 117 (1/28)
2. Llevar **7 bicis** de 256 (21/23) a 026 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

788 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.237 | 0.082 |
| Persistencia | 0.240 | 0.059 |
| Persistencia 0/1 | 0.240 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
