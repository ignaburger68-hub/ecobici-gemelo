# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 11:29 (hora de Ciudad de México).

## Último pronóstico: 17/11 11:29 a 12:29

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.01 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.98 | 0.01 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.83 | 0.03 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.81 | 0.00 | 0-7 |
| 116 Londres-Roma | 1 / 18 | 0.80 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 4 / 31 | 0.73 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 20 | 0.57 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (19/30) a 555 (4/31)
2. Llevar **7 bicis** de 008 (15/16) a 256 (0/19)
3. Llevar **9 bicis** de 107-108 (17/50) a 270 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

33 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.160 | 0.041 |
| Sin resincronizar | 0.196 | 0.091 |
| Persistencia | 0.301 | 0.092 |
| Persistencia 0/1 | 0.301 | 0.092 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
