# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 08:21 (hora de Ciudad de México).

## Último pronóstico: 17/11 08:21 a 09:21

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**12.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.01 | 0-1 |
| 270 De la República-Ponciano Arr | 1 / 26 | 1.00 | 0.00 | 0-1 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 22 | 1.00 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 1.00 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (27/28) a 270 (1/26)
2. Llevar **16 bicis** de 029 (25/29) a 555 (0/31)
3. Llevar **11 bicis** de 008 (12/17) a 259 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

20 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.090 | 0.049 |
| Sin resincronizar | 0.126 | 0.055 |
| Persistencia | 0.311 | 0.130 |
| Persistencia 0/1 | 0.311 | 0.130 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
