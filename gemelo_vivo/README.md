# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 10:40 (hora de Ciudad de México).

## Último pronóstico: 24/11 10:40 a 11:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · lluvia 0.4 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 1.00 | 15-19 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 22 / 22 | 0.00 | 0.99 | 15-22 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 11-15 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.96 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.89 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.84 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 11 | 0.84 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.83 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.82 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 118 (19/19) a 270 (1/27)
2. Llevar **9 bicis** de 113 (15/15) a 086 (0/15)
3. Llevar **12 bicis** de 114 (22/22) a 041 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

527 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.085 |
| Persistencia | 0.276 | 0.060 |
| Persistencia 0/1 | 0.276 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
