# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 22:38 (hora de Ciudad de México).

## Último pronóstico: 20/11 22:38 a 23:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 115 Roma-Dinamarca | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.95 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.77 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.66 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.62 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 15 | 0.40 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 3 / 21 | 0.29 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 7 / 10 | 0.13 | 0.01 | 0-7 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 029 (28/31) a 086 (1/14)
2. Llevar **9 bicis** de 555 (19/30) a 270 (0/27)
3. Llevar **11 bicis** de 450 (20/28) a 115 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

293 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.261 | 0.092 |
| Persistencia | 0.299 | 0.067 |
| Persistencia 0/1 | 0.299 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
