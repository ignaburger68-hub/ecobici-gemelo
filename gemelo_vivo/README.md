# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 08:01 (hora de Ciudad de México).

## Último pronóstico: 26/11 08:00 a 09:00

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
| 117 Londres-Nápoles | 0 / 4 | 0.71 | 1.00 | 4-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.89 | 0.99 | 2-2 |
| 112 Av. Morelos-Abraham González | 0 / 18 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 24 | 0.98 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 2 / 21 | 0.96 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 3 / 15 | 0.88 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 29 | 0.79 | 0.00 | 5-17 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 115 (12/25) a 555 (2/24)
2. Llevar **11 bicis** de 260 (19/21) a 086 (0/16)
3. Llevar **10 bicis** de 119 (16/27) a 041 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

658 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.243 | 0.082 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
