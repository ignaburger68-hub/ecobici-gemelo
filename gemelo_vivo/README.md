# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 17:33 (hora de Ciudad de México).

## Último pronóstico: 25/11 17:33 a 18:33

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
| 012 Río Lerma - Villalongín | 0 / 13 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 10 / 10 | 0.04 | 0.99 | 3-10 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.97 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 4 / 23 | 0.97 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 5 / 28 | 0.96 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 5 / 28 | 0.96 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 1 / 8 | 0.95 | 0.02 | 0-2 |
| 114 Lucerna-Abraham González | 5 / 22 | 0.87 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 048 (10/10) a 031 (5/28)
2. Llevar **10 bicis** de 098 (11/31) a 115 (4/23)
3. Llevar **11 bicis** de 116 (16/22) a 117 (5/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

627 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.243 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
