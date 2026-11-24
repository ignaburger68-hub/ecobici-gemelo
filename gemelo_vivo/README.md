# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 06:53 (hora de Ciudad de México).

## Último pronóstico: 24/11 06:53 a 07:53

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
| 114 Lucerna-Abraham González | 0 / 19 | 0.97 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.95 | 0.00 | 1-8 |
| 116 Londres-Roma | 0 / 17 | 0.92 | 0.00 | 2-9 |
| 555 Ribera de San Cosme - Insurg | 8 / 30 | 0.88 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.86 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 5 / 16 | 0.84 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 0 / 23 | 0.83 | 0.01 | 4-15 |
| 107-108 Tolsa-Balderas | 11 / 53 | 0.68 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 2 / 30 | 0.55 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 1 / 16 | 0.50 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 263 (27/29) a 555 (8/30)
2. Llevar **9 bicis** de 118 (9/19) a 086 (5/16)
3. Llevar **12 bicis** de 010 (15/24) a 107-108 (11/53)

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
