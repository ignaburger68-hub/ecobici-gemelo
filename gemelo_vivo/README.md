# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 22:17 (hora de Ciudad de México).

## Último pronóstico: 18/11 22:17 a 23:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 19 / 19 | 0.00 | 0.99 | 16-19 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.98 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 14 | 0.98 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 9 / 9 | 0.01 | 0.95 | 4-9 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.75 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 14 | 0.75 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 1 / 29 | 0.74 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 15 / 29 | 0.00 | 0.74 | 23-29 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 555 (15/29) a 031 (0/34)
2. Llevar **10 bicis** de 112 (19/19) a 115 (0/24)
3. Llevar **8 bicis** de 450 (22/25) a 020 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

149 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.034 |
| Sin resincronizar | 0.298 | 0.091 |
| Persistencia | 0.340 | 0.068 |
| Persistencia 0/1 | 0.340 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
