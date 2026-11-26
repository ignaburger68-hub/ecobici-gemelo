# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 18:46 (hora de Ciudad de México).

## Último pronóstico: 25/11 18:46 a 19:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 11 | 0.99 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 12 | 0.98 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.97 | 0.00 | 0-8 |
| 555 Ribera de San Cosme - Insurg | 21 / 25 | 0.00 | 0.97 | 22-25 |
| 029 Reforma - Bucareli | 27 / 29 | 0.00 | 0.96 | 24-29 |
| 117 Londres-Nápoles | 1 / 29 | 0.93 | 0.00 | 1-11 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.91 | 16-21 |
| 010 Reforma - Ramírez | 1 / 25 | 0.90 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 555 (21/25) a 010 (1/25)
2. Llevar **17 bicis** de 029 (27/29) a 003 (0/27)
3. Llevar **9 bicis** de 260 (20/21) a 008 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

632 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
