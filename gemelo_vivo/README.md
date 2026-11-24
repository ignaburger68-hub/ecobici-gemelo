# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 08:04 (hora de Ciudad de México).

## Último pronóstico: 24/11 08:04 a 09:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 23 | 0.99 | 0.00 | 1-12 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.99 | 10-18 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 18 | 0.98 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 2 / 21 | 0.97 | 0.00 | 0-2 |
| 107-108 Tolsa-Balderas | 5 / 55 | 0.97 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.96 | 13-15 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.94 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 5 / 27 | 0.94 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 113 (14/15) a 107-108 (5/55)
2. Llevar **12 bicis** de 118 (19/19) a 086 (1/15)
3. Llevar **13 bicis** de 115 (15/26) a 256 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

516 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.087 |
| Persistencia | 0.276 | 0.059 |
| Persistencia 0/1 | 0.276 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
