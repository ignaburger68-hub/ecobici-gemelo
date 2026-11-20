# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 20:40 (hora de Ciudad de México).

## Último pronóstico: 19/11 20:40 a 21:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.76** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.99 | 14-20 |
| 117 Londres-Nápoles | 0 / 25 | 0.97 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 19 | 0.83 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 3 / 26 | 0.82 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 15 | 0.81 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 30 | 0.80 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.78 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.72 | 8-14 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.71 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (20/20) a 010 (3/26)
2. Llevar **8 bicis** de 026 (13/15) a 117 (0/25)
3. Llevar **10 bicis** de 555 (23/27) a 003 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

214 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.295 | 0.097 |
| Persistencia | 0.333 | 0.067 |
| Persistencia 0/1 | 0.333 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
