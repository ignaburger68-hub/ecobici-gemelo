# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 06:41 (hora de Ciudad de México).

## Último pronóstico: 17/11 06:41 a 07:41

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**11.3 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.01 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 19 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 2 / 31 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 3 / 52 | 0.97 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 13 / 16 | 0.00 | 0.95 | 15-16 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.95 | 0.00 | 3-12 |
| 119 Turín-Abraham González | 1 / 25 | 0.84 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (13/16) a 555 (2/31)
2. Llevar **15 bicis** de 010 (17/27) a 107-108 (3/52)
3. Llevar **9 bicis** de 012 (14/15) a 263 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

14 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | nan | nan |
| Sin resincronizar | nan | nan |
| Persistencia | nan | nan |
| Persistencia 0/1 | nan | nan |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
