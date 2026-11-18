# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 12:50 (hora de Ciudad de México).

## Último pronóstico: 18/11 12:50 a 13:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.7 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 18 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.93 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.82 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 2 / 19 | 0.81 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.77 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 31 / 32 | 0.00 | 0.77 | 22-31 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.76 | 22-30 |
| 255 José Rosas Moreno-Guillermo  | 2 / 31 | 0.76 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (31/32) a 041 (2/24)
2. Llevar **13 bicis** de 117 (29/30) a 263 (0/29)
3. Llevar **5 bicis** de 008 (13/14) a 259 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

110 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.028 |
| Sin resincronizar | 0.307 | 0.083 |
| Persistencia | 0.347 | 0.053 |
| Persistencia 0/1 | 0.347 | 0.053 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
