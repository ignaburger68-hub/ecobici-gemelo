# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 06:27 (hora de Ciudad de México).

## Último pronóstico: 17/11 06:27 a 07:27

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**10.8 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 098 Emilio Dondé-Av. Balderas | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.99 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.96 | 0.00 | 2-9 |
| 107-108 Tolsa-Balderas | 3 / 53 | 0.93 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.85 | 0.06 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.79 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 11 / 16 | 0.00 | 0.70 | 13-16 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (11/16) a 555 (1/31)
2. Llevar **14 bicis** de 010 (16/27) a 107-108 (3/53)
3. Llevar **7 bicis** de 012 (13/15) a 085 (0/14)

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
