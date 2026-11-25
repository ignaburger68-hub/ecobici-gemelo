# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 14:14 (hora de Ciudad de México).

## Último pronóstico: 25/11 14:14 a 15:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.97 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.82 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.78 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.78 | 0.00 | 0-10 |
| 116 Londres-Roma | 21 / 23 | 0.00 | 0.75 | 16-23 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.73 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 3 / 22 | 0.67 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.67 | 0.00 | 0-9 |
| 086 Sullivan-Insurgentes | 3 / 17 | 0.66 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (21/23) a 270 (1/25)
2. Llevar **12 bicis** de 031 (31/34) a 256 (3/22)
3. Llevar **12 bicis** de 117 (28/30) a 555 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

613 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.263 | 0.059 |
| Persistencia 0/1 | 0.263 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
