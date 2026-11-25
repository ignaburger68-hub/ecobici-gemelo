# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 15:25 (hora de Ciudad de México).

## Último pronóstico: 25/11 15:25 a 16:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.7 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 0 / 29 | 0.96 | 0.00 | 1-9 |
| 118 Liverpool-Dinamarca | 1 / 19 | 0.93 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.92 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.88 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.86 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.84 | 0.01 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.82 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 25 | 0.81 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (22/23) a 118 (1/19)
2. Llevar **14 bicis** de 031 (30/34) a 270 (0/26)
3. Llevar **11 bicis** de 117 (25/31) a 260 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

618 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
