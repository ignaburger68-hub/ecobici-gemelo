# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 08:29 (hora de Ciudad de México).

## Último pronóstico: 27/11 08:29 a 09:29

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
| 026 Reforma - Versalles | 0 / 1 | 0.91 | 1.00 | 1-1 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.98 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 0 / 17 | 0.97 | 0.00 | 1-9 |
| 113 General Prim-Versalles | 12 / 15 | 0.00 | 0.94 | 13-15 |
| 107-108 Tolsa-Balderas | 0 / 28 | 0.91 | 0.00 | 3-11 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.81 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 19 / 29 | 0.00 | 0.72 | 24-29 |
| 048 Independencia - Azueta | 8 / 9 | 0.02 | 0.65 | 4-9 |
| 555 Ribera de San Cosme - Insurg | 4 / 34 | 0.63 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 113 (12/15) a 041 (0/29)
2. Llevar **17 bicis** de 117 (19/29) a 555 (4/34)
3. Llevar **9 bicis** de 115 (14/24) a 086 (2/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

732 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
