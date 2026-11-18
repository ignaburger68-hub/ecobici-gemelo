# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 12:36 (hora de Ciudad de México).

## Último pronóstico: 18/11 12:36 a 13:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.7 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.94 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.93 | 10-20 |
| 041 Reforma - Av. de la Repúblic | 3 / 24 | 0.91 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 53 | 0.91 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 9 | 0.89 | 0.02 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.87 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.85 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.77 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (31/32) a 041 (3/24)
2. Llevar **14 bicis** de 117 (27/29) a 256 (0/19)
3. Llevar **9 bicis** de 115 (21/21) a 270 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

109 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.028 |
| Sin resincronizar | 0.307 | 0.083 |
| Persistencia | 0.349 | 0.053 |
| Persistencia 0/1 | 0.349 | 0.053 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
