# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 20:24 (hora de Ciudad de México).

## Último pronóstico: 24/11 20:24 a 21:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · lluvia 1.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.50** y las **devoluciones por 0.57** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 17-20 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 28 / 29 | 0.00 | 0.83 | 27-29 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.71 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 21 / 23 | 0.00 | 0.58 | 19-23 |
| 450 Ramos Arizpe- Av México Teno | 24 / 27 | 0.00 | 0.53 | 23-27 |
| 555 Ribera de San Cosme - Insurg | 26 / 31 | 0.00 | 0.45 | 24-31 |
| 086 Sullivan-Insurgentes | 11 / 16 | 0.00 | 0.40 | 10-16 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.34 | 0.00 | 0-4 |
| 116 Londres-Roma | 2 / 23 | 0.31 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (20/20) a 003 (1/27)
2. Llevar **7 bicis** de 098 (28/29) a 113 (0/15)
3. Llevar **10 bicis** de 555 (26/31) a 116 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

568 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.033 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
