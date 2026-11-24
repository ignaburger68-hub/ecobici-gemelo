# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 06:39 (hora de Ciudad de México).

## Último pronóstico: 24/11 06:39 a 07:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 1-6 |
| 116 Londres-Roma | 0 / 19 | 0.95 | 0.00 | 2-9 |
| 086 Sullivan-Insurgentes | 3 / 16 | 0.95 | 0.00 | 0-2 |
| 029 Reforma - Bucareli | 0 / 25 | 0.90 | 0.00 | 3-15 |
| 555 Ribera de San Cosme - Insurg | 10 / 32 | 0.75 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 16 | 0.58 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 13 / 54 | 0.52 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (29/31) a 086 (3/16)
2. Llevar **18 bicis** de 263 (27/29) a 555 (10/32)
3. Llevar **7 bicis** de 118 (8/19) a 041 (0/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

511 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.245 | 0.087 |
| Persistencia | 0.278 | 0.060 |
| Persistencia 0/1 | 0.278 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
