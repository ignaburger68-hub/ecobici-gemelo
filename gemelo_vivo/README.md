# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 07:07 (hora de Ciudad de México).

## Último pronóstico: 24/11 07:07 a 08:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.6 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 20 | 0.96 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 5 / 32 | 0.94 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.94 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 22 | 0.93 | 0.00 | 2-9 |
| 107-108 Tolsa-Balderas | 7 / 54 | 0.92 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 2 / 32 | 0.88 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 13 | 0.87 | 0.13 | 3-13 |
| 118 Liverpool-Dinamarca | 14 / 19 | 0.00 | 0.85 | 12-19 |
| 029 Reforma - Bucareli | 0 / 25 | 0.81 | 0.02 | 6-19 |
| 112 Av. Morelos-Abraham González | 2 / 20 | 0.78 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 118 (14/19) a 555 (5/32)
2. Llevar **17 bicis** de 263 (28/29) a 107-108 (7/54)
3. Llevar **11 bicis** de 450 (30/31) a 086 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

512 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.244 | 0.087 |
| Persistencia | 0.278 | 0.060 |
| Persistencia 0/1 | 0.278 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
