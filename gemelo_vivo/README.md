# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 15:16 (hora de Ciudad de México).

## Último pronóstico: 17/11 15:16 a 16:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 17 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.98 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 9 | 0.95 | 0.01 | 0-4 |
| 115 Roma-Dinamarca | 1 / 24 | 0.94 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 9 | 0.92 | 0.03 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 20 | 0.89 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 117 (20/30) a 010 (0/27)
2. Llevar **8 bicis** de 098 (12/30) a 115 (1/24)
3. Llevar **6 bicis** de 031 (10/26) a 118 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

49 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.031 |
| Sin resincronizar | 0.235 | 0.094 |
| Persistencia | 0.311 | 0.057 |
| Persistencia 0/1 | 0.311 | 0.057 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
