# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 17:49 (hora de Ciudad de México).

## Último pronóstico: 19/11 17:49 a 18:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 031 Hamburgo - Insurgentes | 2 / 32 | 0.99 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.97 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 12 | 0.95 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 22 | 0.94 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 17 / 19 | 0.00 | 0.89 | 15-19 |
| 010 Reforma - Ramírez | 2 / 27 | 0.88 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 3 / 13 | 0.88 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 3 / 14 | 0.77 | 0.00 | 0-5 |
| 116 Londres-Roma | 17 / 19 | 0.00 | 0.73 | 11-19 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 260 (17/19) a 031 (2/32)
2. Llevar **9 bicis** de 116 (17/19) a 270 (1/22)
3. Llevar **9 bicis** de 555 (14/28) a 010 (2/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

202 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
