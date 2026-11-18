# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 18:50 (hora de Ciudad de México).

## Último pronóstico: 17/11 18:50 a 19:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.4 °C** · lluvia 0.1 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 1-8 |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.11 | 0-4 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 1 / 25 | 0.99 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 555 (25/28) a 115 (0/24)
2. Llevar **9 bicis** de 260 (14/17) a 116 (3/16)
3. Llevar **7 bicis** de 450 (9/27) a 118 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

64 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.146 | 0.027 |
| Sin resincronizar | 0.302 | 0.089 |
| Persistencia | 0.366 | 0.045 |
| Persistencia 0/1 | 0.366 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
