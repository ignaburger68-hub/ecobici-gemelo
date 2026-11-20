# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 07:22 (hora de Ciudad de México).

## Último pronóstico: 20/11 07:22 a 08:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.9 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 11 / 11 | 0.12 | 0.99 | 1-10 |
| 555 Ribera de San Cosme - Insurg | 2 / 24 | 0.98 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 2 / 28 | 0.95 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 3 / 16 | 0.80 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.79 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 3 / 19 | 0.71 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 30 | 0.64 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 2 / 11 | 0.56 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 16 / 54 | 0.54 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (12/19) a 555 (2/24)
2. Llevar **12 bicis** de 259 (21/25) a 263 (2/28)
3. Llevar **5 bicis** de 012 (11/11) a 086 (3/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

229 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.287 | 0.095 |
| Persistencia | 0.325 | 0.064 |
| Persistencia 0/1 | 0.325 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
