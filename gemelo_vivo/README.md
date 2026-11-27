# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 07:04 (hora de Ciudad de México).

## Último pronóstico: 27/11 07:03 a 08:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 5 | 0.92 | 0.41 | 1-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 25 | 0.92 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 21 | 0.91 | 0.00 | 3-11 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.76 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 27 / 28 | 0.00 | 0.67 | 21-27 |
| 010 Reforma - Ramírez | 5 / 25 | 0.63 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 3 / 17 | 0.63 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 2 / 21 | 0.58 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (27/28) a 041 (1/25)
2. Llevar **12 bicis** de 259 (19/26) a 010 (5/25)
3. Llevar **7 bicis** de 450 (20/23) a 012 (2/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

726 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.254 | 0.061 |
| Persistencia 0/1 | 0.254 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
