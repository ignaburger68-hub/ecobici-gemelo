# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 18:02 (hora de Ciudad de México).

## Último pronóstico: 25/11 18:02 a 19:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · sin lluvia · viento 5 km/h · día hábil

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
| 115 Roma-Dinamarca | 1 / 24 | 1.00 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 2 / 29 | 0.99 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 4 / 29 | 0.98 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.98 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.98 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 10 / 10 | 0.04 | 0.96 | 4-10 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (18/28) a 031 (2/29)
2. Llevar **13 bicis** de 256 (17/22) a 117 (4/29)
3. Llevar **8 bicis** de 048 (10/10) a 115 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

629 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.244 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
