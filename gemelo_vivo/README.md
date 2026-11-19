# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 07:06 (hora de Ciudad de México).

## Último pronóstico: 19/11 07:06 a 08:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.2 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 14 | 0.96 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 1 / 11 | 0.96 | 0.01 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.95 | 0.00 | 1-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.95 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.90 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 2 / 18 | 0.82 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 1 / 18 | 0.74 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 6 / 14 | 0.00 | 0.69 | 8-14 |

### Plan recomendado del camión

1. Llevar **6 bicis** de 118 (6/14) a 086 (1/11)
2. Llevar **9 bicis** de 029 (12/35) a 041 (1/24)
3. Llevar **11 bicis** de 107-108 (36/52) a 555 (12/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

157 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.289 | 0.092 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
