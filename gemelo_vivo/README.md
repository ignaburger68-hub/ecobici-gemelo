# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 07:38 (hora de Ciudad de México).

## Último pronóstico: 20/11 07:38 a 08:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 24 | 1.00 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 11 / 11 | 0.25 | 0.94 | 0-9 |
| 256 Gómez Farías-Sadi Carnot | 1 / 20 | 0.94 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.89 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 13 / 56 | 0.77 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 2 / 11 | 0.67 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 2 / 28 | 0.64 | 0.03 | 6-22 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 118 (14/19) a 555 (0/24)
2. Llevar **11 bicis** de 029 (16/32) a 263 (0/28)
3. Llevar **12 bicis** de 259 (23/25) a 107-108 (13/56)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

230 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.287 | 0.094 |
| Persistencia | 0.325 | 0.064 |
| Persistencia 0/1 | 0.325 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
