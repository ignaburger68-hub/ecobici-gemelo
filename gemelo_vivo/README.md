# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 06:54 (hora de Ciudad de México).

## Último pronóstico: 20/11 06:54 a 07:54

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
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 20 | 0.96 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 0 / 28 | 0.95 | 0.00 | 0-10 |
| 555 Ribera de San Cosme - Insurg | 4 / 22 | 0.92 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 10 / 11 | 0.00 | 0.79 | 6-11 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.55 | 0.00 | 1-9 |
| 263 Sadi Carnot - Gómez Farias | 4 / 28 | 0.52 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.48 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 010 (15/25) a 555 (4/22)
2. Llevar **6 bicis** de 012 (10/11) a 114 (0/21)
3. Llevar **8 bicis** de 259 (20/25) a 116 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

227 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.289 | 0.095 |
| Persistencia | 0.326 | 0.064 |
| Persistencia 0/1 | 0.326 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
