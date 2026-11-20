# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 18:04 (hora de Ciudad de México).

## Último pronóstico: 19/11 18:03 a 19:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 16-20 |
| 115 Roma-Dinamarca | 1 / 23 | 0.99 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 4 / 32 | 0.96 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 14 | 0.94 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.94 | 0.00 | 0-4 |
| 116 Londres-Roma | 19 / 19 | 0.00 | 0.93 | 10-19 |
| 114 Lucerna-Abraham González | 18 / 18 | 0.00 | 0.92 | 10-18 |
| 010 Reforma - Ramírez | 1 / 27 | 0.89 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 260 (20/20) a 031 (4/32)
2. Llevar **12 bicis** de 116 (19/19) a 115 (1/23)
3. Llevar **8 bicis** de 555 (12/29) a 012 (2/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

203 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.300 | 0.096 |
| Persistencia | 0.335 | 0.069 |
| Persistencia 0/1 | 0.335 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
