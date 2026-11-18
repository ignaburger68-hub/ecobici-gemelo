# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 13:34 (hora de Ciudad de México).

## Último pronóstico: 18/11 13:34 a 14:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.97 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 14 / 14 | 0.00 | 0.94 | 8-14 |
| 107-108 Tolsa-Balderas | 1 / 52 | 0.93 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.88 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.87 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 3 / 13 | 0.85 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 1 / 18 | 0.82 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 008 (14/14) a 107-108 (1/52)
2. Llevar **14 bicis** de 117 (28/30) a 041 (0/24)
3. Llevar **13 bicis** de 031 (29/33) a 270 (2/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

113 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.028 |
| Sin resincronizar | 0.305 | 0.082 |
| Persistencia | 0.345 | 0.054 |
| Persistencia 0/1 | 0.345 | 0.054 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
