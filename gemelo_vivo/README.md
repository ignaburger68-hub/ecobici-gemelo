# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 18:27 (hora de Ciudad de México).

## Último pronóstico: 27/11 18:27 a 19:27

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.5 °C** · lluvia 0.5 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 28 / 29 | 0.00 | 0.93 | 26-29 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.89 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 2 / 16 | 0.84 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 1 / 25 | 0.83 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 24 / 25 | 0.00 | 0.77 | 19-25 |
| 117 Londres-Nápoles | 4 / 29 | 0.52 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 7 / 10 | 0.00 | 0.44 | 5-10 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 029 (28/29) a 012 (0/11)
2. Llevar **11 bicis** de 119 (24/25) a 008 (2/16)
3. Llevar **5 bicis** de 048 (7/10) a 026 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

774 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.240 | 0.081 |
| Persistencia | 0.244 | 0.060 |
| Persistencia 0/1 | 0.244 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
