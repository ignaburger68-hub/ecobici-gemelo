# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 07:49 (hora de Ciudad de México).

## Último pronóstico: 19/11 07:49 a 08:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 11 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 23 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 255 José Rosas Moreno-Guillermo  | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 18 | 0.99 | 0.00 | 1-8 |
| 010 Reforma - Ramírez | 0 / 24 | 0.99 | 0.00 | 0-9 |
| 118 Liverpool-Dinamarca | 14 / 14 | 0.03 | 0.99 | 4-13 |
| 112 Av. Morelos-Abraham González | 0 / 18 | 0.98 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (14/14) a 259 (1/23)
2. Llevar **9 bicis** de 026 (10/15) a 086 (0/11)
3. Llevar **6 bicis** de 115 (6/24) a 555 (4/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

160 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.285 | 0.091 |
| Persistencia | 0.332 | 0.068 |
| Persistencia 0/1 | 0.332 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
