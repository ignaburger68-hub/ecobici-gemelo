# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 21:35 (hora de Ciudad de México).

## Último pronóstico: 18/11 21:35 a 22:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 031 Hamburgo - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 13 | 0.99 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.93 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 2 / 13 | 0.83 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 1 / 11 | 0.82 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 22 | 0.77 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 21 / 25 | 0.00 | 0.76 | 22-25 |
| 117 Londres-Nápoles | 2 / 29 | 0.70 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 2 / 29 | 0.69 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 450 (21/25) a 031 (0/30)
2. Llevar **13 bicis** de 112 (17/19) a 270 (2/26)
3. Llevar **9 bicis** de 255 (22/30) a 116 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

146 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.034 |
| Sin resincronizar | 0.301 | 0.089 |
| Persistencia | 0.342 | 0.068 |
| Persistencia 0/1 | 0.342 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
