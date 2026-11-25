# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 13:31 (hora de Ciudad de México).

## Último pronóstico: 25/11 13:31 a 14:31

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
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.99 | 0.00 | 0-8 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.83 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.80 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.78 | 0.00 | 0-5 |
| 116 Londres-Roma | 21 / 22 | 0.00 | 0.74 | 15-22 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.73 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.70 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 116 (21/22) a 041 (0/31)
2. Llevar **12 bicis** de 031 (30/34) a 086 (0/17)
3. Llevar **14 bicis** de 117 (26/31) a 555 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

610 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.264 | 0.060 |
| Persistencia 0/1 | 0.264 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
