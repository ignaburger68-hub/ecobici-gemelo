# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 20:23 (hora de Ciudad de México).

## Último pronóstico: 26/11 20:23 a 21:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.67** y las **devoluciones por 0.74** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 0 / 13 | 1.00 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.87 | 0.99 | 2-2 |
| 256 Gómez Farías-Sadi Carnot | 18 / 18 | 0.00 | 0.96 | 10-17 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.88 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.79 | 13-20 |
| 010 Reforma - Ramírez | 5 / 26 | 0.69 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 3 / 21 | 0.64 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 7 / 9 | 0.01 | 0.56 | 4-9 |
| 114 Lucerna-Abraham González | 2 / 21 | 0.55 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 256 (18/18) a 113 (0/13)
2. Llevar **12 bicis** de 260 (19/20) a 010 (5/26)
3. Llevar **9 bicis** de 029 (27/29) a 012 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

710 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.249 | 0.082 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
