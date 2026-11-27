# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 08:00 (hora de Ciudad de México).

## Último pronóstico: 27/11 08:00 a 09:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · lluvia 0.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.76** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 3 | 0.84 | 0.97 | 3-3 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.94 | 0.00 | 1-11 |
| 107-108 Tolsa-Balderas | 0 / 25 | 0.90 | 0.00 | 2-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 26 | 0.86 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 13 | 0.84 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 5 / 13 | 0.00 | 0.54 | 7-13 |
| 003 Reforma - Insurgentes | 3 / 25 | 0.34 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 5 / 14 | 0.33 | 0.02 | 0-9 |
| 048 Independencia - Azueta | 7 / 9 | 0.05 | 0.30 | 2-9 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 113 (5/13) a 086 (1/13)
2. Llevar **6 bicis** de 117 (7/27) a 041 (1/26)
3. Llevar **4 bicis** de 010 (12/26) a 114 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

730 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
