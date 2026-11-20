# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 07:52 (hora de Ciudad de México).

## Último pronóstico: 20/11 07:52 a 08:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.99 | 0.00 | 1-9 |
| 107-108 Tolsa-Balderas | 2 / 55 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 2 / 26 | 0.96 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.93 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 29 | 0.75 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 3 / 25 | 0.74 | 0.00 | 1-11 |
| 260 Av. Juárez-Balderas | 9 / 18 | 0.55 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 259 (23/25) a 107-108 (2/55)
2. Llevar **9 bicis** de 098 (14/29) a 555 (2/26)
3. Llevar **4 bicis** de 026 (4/14) a 263 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

231 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.286 | 0.094 |
| Persistencia | 0.324 | 0.064 |
| Persistencia 0/1 | 0.324 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
