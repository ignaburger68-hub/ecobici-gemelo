# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 07:18 (hora de Ciudad de México).

## Último pronóstico: 26/11 07:18 a 08:18

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
| 086 Sullivan-Insurgentes | 0 / 16 | 1.00 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.89 | 0.99 | 1-1 |
| 555 Ribera de San Cosme - Insurg | 2 / 26 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.96 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 1 / 32 | 0.95 | 0.00 | 0-8 |
| 029 Reforma - Bucareli | 0 / 24 | 0.93 | 0.01 | 5-17 |
| 117 Londres-Nápoles | 0 / 13 | 0.89 | 0.57 | 7-13 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.83 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 259 (21/25) a 555 (2/26)
2. Llevar **10 bicis** de 118 (11/16) a 086 (0/16)
3. Llevar **11 bicis** de 119 (20/27) a 041 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

655 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.243 | 0.082 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
