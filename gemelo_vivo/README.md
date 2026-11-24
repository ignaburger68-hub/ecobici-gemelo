# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 07:21 (hora de Ciudad de México).

## Último pronóstico: 24/11 07:21 a 08:21

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
| 107-108 Tolsa-Balderas | 5 / 53 | 0.98 | 0.00 | 0-1 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.97 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 4 / 31 | 0.96 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.95 | 0.00 | 1-7 |
| 116 Londres-Roma | 0 / 13 | 0.94 | 0.37 | 6-13 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 20 | 0.93 | 0.00 | 2-8 |
| 029 Reforma - Bucareli | 0 / 23 | 0.91 | 0.05 | 6-19 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.86 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 16 / 19 | 0.00 | 0.85 | 13-19 |
| 112 Av. Morelos-Abraham González | 3 / 20 | 0.76 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 118 (16/19) a 107-108 (5/53)
2. Llevar **15 bicis** de 263 (27/29) a 555 (4/31)
3. Llevar **11 bicis** de 450 (29/31) a 041 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

513 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.244 | 0.087 |
| Persistencia | 0.277 | 0.060 |
| Persistencia 0/1 | 0.277 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
