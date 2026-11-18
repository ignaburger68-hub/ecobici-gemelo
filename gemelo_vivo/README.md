# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 11:25 (hora de Ciudad de México).

## Último pronóstico: 18/11 11:25 a 12:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 32 / 32 | 0.00 | 0.98 | 28-32 |
| 020 Reforma- Río Támesis | 10 / 10 | 0.00 | 0.97 | 6-10 |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.96 | 15-21 |
| 117 Londres-Nápoles | 28 / 30 | 0.00 | 0.83 | 26-30 |
| 118 Liverpool-Dinamarca | 12 / 13 | 0.00 | 0.83 | 9-13 |
| 107-108 Tolsa-Balderas | 1 / 54 | 0.78 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 1 / 19 | 0.77 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.74 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 031 (32/32) a 256 (0/19)
2. Llevar **18 bicis** de 117 (28/30) a 107-108 (1/54)
3. Llevar **7 bicis** de 118 (12/13) a 114 (1/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

104 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.027 |
| Sin resincronizar | 0.308 | 0.084 |
| Persistencia | 0.354 | 0.049 |
| Persistencia 0/1 | 0.354 | 0.049 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
