# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 08:03 (hora de Ciudad de México).

## Último pronóstico: 25/11 08:03 a 09:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

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
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 17 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 0 / 18 | 0.97 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.94 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 4 / 26 | 0.81 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 17 | 0.74 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 118 (14/17) a 086 (0/14)
2. Llevar **8 bicis** de 113 (9/15) a 256 (0/21)
3. Llevar **8 bicis** de 026 (9/14) a 260 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

587 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.082 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
