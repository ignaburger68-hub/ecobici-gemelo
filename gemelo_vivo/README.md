# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 06:21 (hora de Ciudad de México).

## Último pronóstico: 26/11 06:21 a 07:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.8 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 008 Reforma - General Prim | 0 / 12 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.98 | 0.01 | 2-10 |
| 029 Reforma - Bucareli | 0 / 26 | 0.98 | 0.00 | 2-10 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.97 | 0.94 | 1-1 |
| 117 Londres-Nápoles | 0 / 24 | 0.97 | 0.00 | 1-8 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.89 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.80 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 085 (11/13) a 086 (5/16)
2. Llevar **8 bicis** de 010 (11/25) a 114 (1/21)
3. Llevar **13 bicis** de 450 (26/27) a 041 (2/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

653 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.244 | 0.083 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
