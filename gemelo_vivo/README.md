# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 13:23 (hora de Ciudad de México).

## Último pronóstico: 20/11 13:23 a 14:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.1 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 10 / 10 | 0.02 | 0.99 | 4-10 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.99 | 0.00 | 0-6 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.98 | 18-22 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.96 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.96 | 0.01 | 0-6 |
| 010 Reforma - Ramírez | 1 / 25 | 0.89 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.82 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 2 / 34 | 0.80 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 33 / 34 | 0.00 | 0.79 | 26-34 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 116 (22/22) a 041 (0/29)
2. Llevar **14 bicis** de 031 (33/34) a 010 (1/25)
3. Llevar **7 bicis** de 048 (10/10) a 555 (2/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

254 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.274 | 0.091 |
| Persistencia | 0.313 | 0.065 |
| Persistencia 0/1 | 0.313 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
