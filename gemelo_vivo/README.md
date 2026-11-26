# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 14:24 (hora de Ciudad de México).

## Último pronóstico: 26/11 14:24 a 15:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.75** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.98 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 0 / 9 | 0.98 | 0.01 | 0-3 |
| 113 General Prim-Versalles | 14 / 14 | 0.00 | 0.98 | 6-13 |
| 255 José Rosas Moreno-Guillermo  | 0 / 34 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.94 | 10-18 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.92 | 0.49 | 2-6 |
| 107-108 Tolsa-Balderas | 1 / 55 | 0.91 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 12 | 0.86 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (14/14) a 256 (0/23)
2. Llevar **11 bicis** de 260 (19/21) a 041 (0/32)
3. Llevar **15 bicis** de 117 (27/28) a 107-108 (1/55)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

685 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
