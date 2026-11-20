# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 13:37 (hora de Ciudad de México).

## Último pronóstico: 20/11 13:37 a 14:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 4 km/h · día hábil

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
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-6 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 18-22 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.98 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 0 / 33 | 0.97 | 0.00 | 1-9 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.97 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.97 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 29 / 29 | 0.00 | 0.96 | 21-29 |
| 031 Hamburgo - Insurgentes | 33 / 34 | 0.00 | 0.85 | 26-34 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 116 (22/22) a 555 (0/33)
2. Llevar **15 bicis** de 031 (33/34) a 010 (0/25)
3. Llevar **16 bicis** de 117 (29/29) a 041 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

255 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
