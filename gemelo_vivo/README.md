# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 19:04 (hora de Ciudad de México).

## Último pronóstico: 17/11 19:04 a 20:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.4 °C** · lluvia 0.1 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.76** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 23 | 1.00 | 0.01 | 3-13 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.07 | 1-8 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.01 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (17/18) a 119 (0/25)
2. Llevar **9 bicis** de 450 (11/27) a 115 (0/23)
3. Llevar **9 bicis** de 555 (21/29) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

65 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.144 | 0.026 |
| Sin resincronizar | 0.306 | 0.089 |
| Persistencia | 0.370 | 0.045 |
| Persistencia 0/1 | 0.370 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
