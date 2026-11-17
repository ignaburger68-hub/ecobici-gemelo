# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 09:03 (hora de Ciudad de México).

## Último pronóstico: 17/11 09:03 a 10:03

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.01 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (9/10) a 270 (0/25)
2. Llevar **10 bicis** de 008 (14/16) a 107-108 (2/54)
3. Llevar **11 bicis** de 117 (19/30) a 010 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

23 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.131 | 0.043 |
| Sin resincronizar | 0.125 | 0.056 |
| Persistencia | 0.337 | 0.106 |
| Persistencia 0/1 | 0.337 | 0.106 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
