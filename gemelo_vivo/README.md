# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 06:56 (hora de Ciudad de México).

## Último pronóstico: 17/11 06:55 a 07:55

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**11.3 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 118 Liverpool-Dinamarca | 15 / 16 | 0.00 | 1.00 | 11-16 |
| 107-108 Tolsa-Balderas | 1 / 52 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 2 / 31 | 0.99 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 0 / 19 | 0.99 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.98 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.95 | 0.03 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 15 | 0.87 | 0.06 | 3-12 |
| 255 José Rosas Moreno-Guillermo  | 3 / 28 | 0.85 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 118 (15/16) a 107-108 (1/52)
2. Llevar **16 bicis** de 010 (23/27) a 555 (2/31)
3. Llevar **12 bicis** de 116 (17/18) a 263 (0/29)

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
