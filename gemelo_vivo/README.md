# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 20:30 (hora de Ciudad de México).

## Último pronóstico: 17/11 20:30 a 21:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.1 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 25 | 0.99 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 450 (26/27) a 010 (0/27)
2. Llevar **13 bicis** de 255 (20/27) a 003 (0/31)
3. Llevar **11 bicis** de 555 (25/29) a 041 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

71 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.133 | 0.028 |
| Sin resincronizar | 0.318 | 0.091 |
| Persistencia | 0.370 | 0.048 |
| Persistencia 0/1 | 0.370 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
