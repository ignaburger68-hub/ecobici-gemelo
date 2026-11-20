# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 12:36 (hora de Ciudad de México).

## Último pronóstico: 20/11 12:36 a 13:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.4 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 10 / 10 | 0.01 | 0.96 | 6-10 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.96 | 11-19 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.92 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.91 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.91 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.89 | 13-19 |
| 555 Ribera de San Cosme - Insurg | 1 / 34 | 0.89 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (19/20) a 555 (1/34)
2. Llevar **17 bicis** de 031 (33/34) a 041 (1/29)
3. Llevar **17 bicis** de 117 (28/30) a 255 (1/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

251 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.276 | 0.091 |
| Persistencia | 0.315 | 0.065 |
| Persistencia 0/1 | 0.315 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
