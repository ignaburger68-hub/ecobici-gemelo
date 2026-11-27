# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 07:18 (hora de Ciudad de México).

## Último pronóstico: 27/11 07:18 a 08:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.76** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 1 / 25 | 0.95 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 5 | 0.94 | 0.68 | 2-5 |
| 010 Reforma - Ramírez | 4 / 26 | 0.87 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 22 | 0.83 | 0.00 | 3-12 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.74 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 4 / 14 | 0.72 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 5 / 14 | 0.56 | 0.01 | 0-7 |
| 112 Av. Morelos-Abraham González | 4 / 17 | 0.55 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 8 / 20 | 0.55 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 270 (25/28) a 010 (4/26)
2. Llevar **12 bicis** de 259 (20/26) a 041 (1/25)
3. Llevar **6 bicis** de 119 (16/26) a 012 (4/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

727 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
