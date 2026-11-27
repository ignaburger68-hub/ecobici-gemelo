# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 07:46 (hora de Ciudad de México).

## Último pronóstico: 27/11 07:46 a 08:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · lluvia 0.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.99 | 0.00 | 1-9 |
| 107-108 Tolsa-Balderas | 0 / 23 | 0.91 | 0.00 | 2-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 26 | 0.88 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 6 | 0.87 | 0.82 | 4-6 |
| 012 Río Lerma - Villalongín | 6 / 14 | 0.50 | 0.01 | 0-8 |
| 086 Sullivan-Insurgentes | 4 / 12 | 0.47 | 0.05 | 0-8 |
| 113 General Prim-Versalles | 5 / 13 | 0.00 | 0.44 | 7-13 |
| 085 Rosas Moreno - Sullivan | 4 / 11 | 0.44 | 0.01 | 0-6 |
| 003 Reforma - Insurgentes | 3 / 25 | 0.33 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 113 (5/13) a 041 (1/26)
2. Llevar **5 bicis** de 117 (7/28) a 114 (0/21)
3. Llevar **5 bicis** de 270 (22/28) a 012 (6/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

729 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.246 | 0.081 |
| Persistencia | 0.253 | 0.061 |
| Persistencia 0/1 | 0.253 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
