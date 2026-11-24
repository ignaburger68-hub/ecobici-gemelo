# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 06:24 (hora de Ciudad de México).

## Último pronóstico: 24/11 06:24 a 07:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 20 | 1.00 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 9 / 9 | 0.02 | 0.99 | 3-9 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 20 | 0.98 | 0.00 | 1-8 |
| 029 Reforma - Bucareli | 0 / 25 | 0.96 | 0.00 | 3-14 |
| 086 Sullivan-Insurgentes | 2 / 16 | 0.92 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 16 | 0.56 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 11 / 32 | 0.56 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 450 (30/31) a 086 (2/16)
2. Llevar **5 bicis** de 085 (9/9) a 041 (0/32)
3. Llevar **15 bicis** de 263 (28/29) a 555 (11/32)

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
