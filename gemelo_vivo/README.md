# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 21:21 (hora de Ciudad de México).

## Último pronóstico: 18/11 21:20 a 22:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 21 | 0.99 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 13 | 0.98 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 9 | 0.97 | 0.08 | 0-7 |
| 031 Hamburgo - Insurgentes | 1 / 30 | 0.97 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 1 / 13 | 0.95 | 0.00 | 0-1 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.91 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 25 | 0.89 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 22 / 25 | 0.00 | 0.84 | 24-25 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 450 (22/25) a 031 (1/30)
2. Llevar **13 bicis** de 112 (18/19) a 270 (2/25)
3. Llevar **10 bicis** de 263 (22/29) a 118 (1/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

145 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.034 |
| Sin resincronizar | 0.301 | 0.088 |
| Persistencia | 0.343 | 0.068 |
| Persistencia 0/1 | 0.343 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
