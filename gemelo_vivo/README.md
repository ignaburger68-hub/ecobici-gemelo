# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 13:46 (hora de Ciudad de México).

## Último pronóstico: 25/11 13:45 a 14:45

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
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.98 | 0.00 | 1-9 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.93 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.84 | 0.00 | 1-8 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.78 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.72 | 0.00 | 0-6 |
| 116 Londres-Roma | 21 / 23 | 0.00 | 0.67 | 16-23 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 0.67 | 0.00 | 1-11 |
| 003 Reforma - Insurgentes | 3 / 27 | 0.57 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 116 (21/23) a 041 (1/31)
2. Llevar **9 bicis** de 031 (29/34) a 086 (0/17)
3. Llevar **7 bicis** de 117 (23/30) a 012 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

611 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
