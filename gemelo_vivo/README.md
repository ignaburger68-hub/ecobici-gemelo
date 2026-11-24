# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 09:57 (hora de Ciudad de México).

## Último pronóstico: 24/11 09:57 a 10:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 27 | 0.99 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.98 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 14 / 14 | 0.00 | 0.98 | 8-14 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.96 | 9-13 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (18/19) a 041 (0/32)
2. Llevar **9 bicis** de 026 (13/13) a 086 (0/14)
3. Llevar **9 bicis** de 113 (13/15) a 119 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

524 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.241 | 0.086 |
| Persistencia | 0.276 | 0.060 |
| Persistencia 0/1 | 0.276 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
