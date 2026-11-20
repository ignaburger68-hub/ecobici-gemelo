# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 21:14 (hora de Ciudad de México).

## Último pronóstico: 19/11 21:14 a 22:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 7 km/h · día hábil

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
| 041 Reforma - Av. de la Repúblic | 0 / 28 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.98 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.94 | 14-20 |
| 117 Londres-Nápoles | 1 / 26 | 0.86 | 0.00 | 0-3 |
| 116 Londres-Roma | 1 / 20 | 0.79 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 4 / 26 | 0.77 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 2 / 30 | 0.76 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 26 | 0.67 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 2 / 11 | 0.66 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (20/20) a 010 (4/26)
2. Llevar **14 bicis** de 255 (25/30) a 041 (0/28)
3. Llevar **8 bicis** de 555 (19/27) a 003 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

216 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.293 | 0.097 |
| Persistencia | 0.331 | 0.067 |
| Persistencia 0/1 | 0.331 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
