# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 08:15 (hora de Ciudad de México).

## Último pronóstico: 27/11 08:15 a 09:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · lluvia 0.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 107-108 Tolsa-Balderas | 0 / 25 | 0.92 | 0.00 | 3-11 |
| 113 General Prim-Versalles | 9 / 14 | 0.00 | 0.84 | 12-14 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.83 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 2 / 20 | 0.69 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 2 / 28 | 0.69 | 0.00 | 0-7 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.43 | 0.01 | 2-13 |
| 117 Londres-Nápoles | 14 / 28 | 0.00 | 0.42 | 19-28 |
| 555 Ribera de San Cosme - Insurg | 6 / 34 | 0.42 | 0.00 | 1-11 |
| 048 Independencia - Azueta | 7 / 9 | 0.04 | 0.38 | 3-9 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (9/14) a 086 (2/14)
2. Llevar **13 bicis** de 117 (14/28) a 041 (2/28)
3. Llevar **8 bicis** de 115 (11/24) a 020 (2/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

731 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.253 | 0.061 |
| Persistencia 0/1 | 0.253 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
