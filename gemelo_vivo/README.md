# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 14:42 (hora de Ciudad de México).

## Último pronóstico: 25/11 14:42 a 15:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.7 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 1.00 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.98 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.96 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.94 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.92 | 0.01 | 0-9 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.90 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.89 | 0.00 | 0-7 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.76 | 21-29 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 116 (22/23) a 256 (0/22)
2. Llevar **15 bicis** de 117 (29/30) a 041 (0/31)
3. Llevar **12 bicis** de 031 (27/34) a 118 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

615 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.263 | 0.060 |
| Persistencia 0/1 | 0.263 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
