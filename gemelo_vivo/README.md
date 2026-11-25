# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 13:03 (hora de Ciudad de México).

## Último pronóstico: 25/11 13:02 a 14:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.98 | 0.00 | 0-4 |
| 116 Londres-Roma | 23 / 23 | 0.00 | 0.97 | 15-23 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.97 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.96 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 116 (23/23) a 041 (1/31)
2. Llevar **13 bicis** de 115 (22/25) a 270 (0/26)
3. Llevar **16 bicis** de 031 (27/34) a 555 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

608 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
