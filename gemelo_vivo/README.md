# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 14:03 (hora de Ciudad de México).

## Último pronóstico: 18/11 14:03 a 15:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 52 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.98 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 0.95 | 23-30 |
| 020 Reforma- Río Támesis | 1 / 11 | 0.83 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 18 / 19 | 0.00 | 0.80 | 12-19 |
| 029 Reforma - Bucareli | 1 / 29 | 0.79 | 0.00 | 1-9 |
| 048 Independencia - Azueta | 1 / 9 | 0.78 | 0.04 | 0-5 |
| 008 Reforma - General Prim | 13 / 14 | 0.00 | 0.74 | 7-14 |
| 118 Liverpool-Dinamarca | 3 / 13 | 0.72 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (30/30) a 107-108 (0/52)
2. Llevar **14 bicis** de 031 (32/33) a 041 (0/24)
3. Llevar **7 bicis** de 115 (18/19) a 118 (3/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

115 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.029 |
| Sin resincronizar | 0.305 | 0.082 |
| Persistencia | 0.343 | 0.056 |
| Persistencia 0/1 | 0.343 | 0.056 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
