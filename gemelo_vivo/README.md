# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 18:07 (hora de Ciudad de México).

## Último pronóstico: 17/11 18:07 a 19:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.6 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 1 / 24 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.12 | 0-3 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 9 | 1.00 | 0.02 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-7 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 15 | 0.99 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 555 (27/30) a 031 (0/26)
2. Llevar **13 bicis** de 260 (14/18) a 117 (0/29)
3. Llevar **10 bicis** de 107-108 (14/49) a 115 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

61 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.027 |
| Sin resincronizar | 0.288 | 0.090 |
| Persistencia | 0.354 | 0.045 |
| Persistencia 0/1 | 0.354 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
