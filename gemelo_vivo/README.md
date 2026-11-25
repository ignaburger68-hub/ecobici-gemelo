# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 07:49 (hora de Ciudad de México).

## Último pronóstico: 25/11 07:49 a 08:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 18 | 0.98 | 0.00 | 0-5 |
| 116 Londres-Roma | 0 / 21 | 0.91 | 0.02 | 2-14 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.89 | 0.00 | 2-14 |
| 086 Sullivan-Insurgentes | 2 / 13 | 0.89 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 3 / 14 | 0.89 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 5 / 18 | 0.86 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.84 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.77 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (8/15) a 012 (3/14)
2. Llevar **10 bicis** de 270 (24/28) a 260 (5/18)
3. Llevar **13 bicis** de 119 (22/28) a 555 (3/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

586 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.033 |
| Sin resincronizar | 0.238 | 0.082 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
