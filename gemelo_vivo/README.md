# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 22:39 (hora de Ciudad de México).

## Último pronóstico: 19/11 22:39 a 23:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 3 / 28 | 0.76 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.73 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 17 | 0.68 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 19 | 0.66 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 4 / 16 | 0.66 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 259 (21/25) a 263 (3/28)
2. Llevar **9 bicis** de 555 (17/26) a 031 (0/34)
3. Llevar **8 bicis** de 255 (26/30) a 086 (4/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

222 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.290 | 0.096 |
| Persistencia | 0.329 | 0.066 |
| Persistencia 0/1 | 0.329 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
