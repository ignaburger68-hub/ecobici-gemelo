# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 07:32 (hora de Ciudad de México).

## Último pronóstico: 27/11 07:32 a 08:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · lluvia 0.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.73** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 5 | 0.95 | 0.77 | 3-5 |
| 107-108 Tolsa-Balderas | 0 / 21 | 0.88 | 0.00 | 2-10 |
| 041 Reforma - Av. de la Repúblic | 2 / 26 | 0.84 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 4 / 26 | 0.81 | 0.00 | 1-7 |
| 012 Río Lerma - Villalongín | 5 / 15 | 0.70 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 8 / 9 | 0.05 | 0.54 | 3-9 |
| 003 Reforma - Insurgentes | 2 / 25 | 0.53 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 8 / 20 | 0.51 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (25/28) a 010 (4/26)
2. Llevar **8 bicis** de 119 (17/26) a 041 (2/26)
3. Llevar **7 bicis** de 259 (21/26) a 012 (5/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

728 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.246 | 0.081 |
| Persistencia | 0.254 | 0.061 |
| Persistencia 0/1 | 0.254 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
