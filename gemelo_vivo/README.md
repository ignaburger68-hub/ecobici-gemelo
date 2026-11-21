# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 15:29 (hora de Ciudad de México).

## Último pronóstico: 21/11 15:28 a 16:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.5 °C** · sin lluvia · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 27 | 0.86 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.85 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.80 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 27 | 0.75 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.64 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.61 | 0.00 | 0-6 |
| 116 Londres-Roma | 2 / 23 | 0.61 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 2 / 14 | 0.47 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.42 | 0.01 | 0-8 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (25/31) a 041 (0/31)
2. Llevar **13 bicis** de 259 (22/25) a 115 (1/27)
3. Llevar **10 bicis** de 555 (29/34) a 112 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

334 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
