# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 20:11 (hora de Ciudad de México).

## Último pronóstico: 19/11 20:11 a 21:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.97 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.97 | 0.02 | 0-8 |
| 116 Londres-Roma | 0 / 20 | 0.91 | 0.00 | 1-9 |
| 008 Reforma - General Prim | 1 / 16 | 0.84 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 4 / 26 | 0.82 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.82 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 16 / 19 | 0.00 | 0.81 | 15-19 |
| 048 Independencia - Azueta | 7 / 9 | 0.02 | 0.67 | 4-9 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (16/19) a 115 (4/26)
2. Llevar **8 bicis** de 555 (24/31) a 086 (0/15)
3. Llevar **11 bicis** de 255 (24/31) a 118 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

212 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.297 | 0.097 |
| Persistencia | 0.335 | 0.068 |
| Persistencia 0/1 | 0.335 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
