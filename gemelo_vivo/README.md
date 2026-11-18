# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 18:36 (hora de Ciudad de México).

## Último pronóstico: 17/11 18:36 a 19:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.4 °C** · lluvia 0.1 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.87** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 6 | 1.00 | 0.08 | 0-2 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 555 (28/29) a 031 (0/26)
2. Llevar **12 bicis** de 260 (17/18) a 115 (1/24)
3. Llevar **7 bicis** de 107-108 (11/48) a 020 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

63 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.027 |
| Sin resincronizar | 0.297 | 0.089 |
| Persistencia | 0.360 | 0.044 |
| Persistencia 0/1 | 0.360 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
