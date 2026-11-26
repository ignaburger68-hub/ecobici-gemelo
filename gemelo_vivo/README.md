# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 07:46 (hora de Ciudad de México).

## Último pronóstico: 26/11 07:46 a 08:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.91 | 1.00 | 1-1 |
| 086 Sullivan-Insurgentes | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 2 / 15 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 2 / 26 | 0.97 | 0.00 | 0-2 |
| 112 Av. Morelos-Abraham González | 1 / 18 | 0.97 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.88 | 0.00 | 0-7 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.86 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 119 (19/27) a 555 (2/26)
2. Llevar **10 bicis** de 098 (14/30) a 012 (2/15)
3. Llevar **9 bicis** de 259 (20/25) a 086 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

657 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.243 | 0.082 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
