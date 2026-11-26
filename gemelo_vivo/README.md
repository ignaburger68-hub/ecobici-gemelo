# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 06:49 (hora de Ciudad de México).

## Último pronóstico: 26/11 06:49 a 07:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.2 °C** · sin lluvia · viento 1 km/h · día hábil

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
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.90 | 0.99 | 1-1 |
| 112 Av. Morelos-Abraham González | 0 / 18 | 0.97 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 3 / 16 | 0.95 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 7 / 27 | 0.93 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 0 / 21 | 0.90 | 0.01 | 3-13 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 119 (21/27) a 555 (7/27)
2. Llevar **12 bicis** de 098 (18/30) a 086 (3/16)
3. Llevar **9 bicis** de 259 (19/26) a 114 (0/21)

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
