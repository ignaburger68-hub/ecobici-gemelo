# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 07:21 (hora de Ciudad de México).

## Último pronóstico: 19/11 07:21 a 08:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 11 | 1.00 | 0.01 | 0-3 |
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 37 | 0.99 | 0.00 | 1-10 |
| 114 Lucerna-Abraham González | 0 / 18 | 0.98 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 13 / 14 | 0.00 | 0.98 | 10-14 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.94 | 0.00 | 0-10 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 23 | 0.85 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 118 (13/14) a 256 (0/18)
2. Llevar **8 bicis** de 029 (11/35) a 086 (0/11)
3. Llevar **6 bicis** de 026 (6/15) a 041 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

158 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.287 | 0.091 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
