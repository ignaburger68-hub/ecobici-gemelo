# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 15:25 (hora de Ciudad de México).

## Último pronóstico: 26/11 15:25 a 16:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · lluvia 0.3 mm/h · viento 3 km/h · día hábil

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
| 010 Reforma - Ramírez | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 9 | 0.98 | 0.01 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.94 | 10-18 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.92 | 0.75 | 3-5 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.90 | 15-25 |
| 029 Reforma - Bucareli | 0 / 6 | 0.82 | 0.89 | 5-6 |
| 008 Reforma - General Prim | 2 / 12 | 0.81 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 32 | 0.73 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (19/19) a 010 (0/24)
2. Llevar **12 bicis** de 117 (27/27) a 041 (0/30)
3. Llevar **6 bicis** de 260 (19/21) a 048 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

689 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.248 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
