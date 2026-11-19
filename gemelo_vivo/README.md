# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 16:38 (hora de Ciudad de México).

## Último pronóstico: 19/11 16:38 a 17:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.99 | 11-17 |
| 115 Roma-Dinamarca | 0 / 21 | 0.98 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.96 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 27 | 0.96 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.95 | 0.02 | 0-9 |
| 031 Hamburgo - Insurgentes | 4 / 29 | 0.86 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.81 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 114 (17/17) a 010 (1/27)
2. Llevar **7 bicis** de 260 (8/20) a 115 (0/21)
3. Llevar **8 bicis** de 029 (13/31) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

197 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.297 | 0.095 |
| Persistencia | 0.335 | 0.070 |
| Persistencia 0/1 | 0.335 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
