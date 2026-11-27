# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 17:58 (hora de Ciudad de México).

## Último pronóstico: 27/11 17:58 a 18:58

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.5 °C** · lluvia 0.5 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.62** y las **devoluciones por 0.69** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 1.00 | 28-31 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 14 | 0.98 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 24 / 25 | 0.00 | 0.79 | 20-25 |
| 010 Reforma - Ramírez | 1 / 25 | 0.73 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 23 | 0.71 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 2 / 18 | 0.64 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 4 / 16 | 0.34 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 5 / 30 | 0.28 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 029 (31/31) a 026 (0/14)
2. Llevar **7 bicis** de 119 (24/25) a 012 (0/11)
3. Llevar **13 bicis** de 029 (31/31) a 115 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

772 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.241 | 0.081 |
| Persistencia | 0.245 | 0.060 |
| Persistencia 0/1 | 0.245 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
