# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 10:11 (hora de Ciudad de México).

## Último pronóstico: 24/11 10:11 a 11:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.99 | 14-19 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 10-15 |
| 119 Turín-Abraham González | 0 / 26 | 0.98 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 22 | 0.97 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.83 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.83 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 118 (19/19) a 048 (0/11)
2. Llevar **9 bicis** de 113 (15/15) a 086 (0/15)
3. Llevar **11 bicis** de 114 (20/22) a 041 (0/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

525 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.241 | 0.086 |
| Persistencia | 0.276 | 0.060 |
| Persistencia 0/1 | 0.276 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
