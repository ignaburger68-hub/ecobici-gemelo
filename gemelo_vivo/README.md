# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 09:26 (hora de Ciudad de México).

## Último pronóstico: 27/11 09:26 a 10:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.1 °C** · lluvia 0.2 mm/h · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 1.00 | 12-16 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.98 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.96 | 12-15 |
| 118 Liverpool-Dinamarca | 18 / 19 | 0.00 | 0.92 | 15-19 |
| 012 Río Lerma - Villalongín | 13 / 14 | 0.00 | 0.91 | 10-14 |
| 107-108 Tolsa-Balderas | 0 / 30 | 0.90 | 0.00 | 2-10 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.89 | 5-10 |
| 086 Sullivan-Insurgentes | 2 / 16 | 0.75 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 29 | 0.70 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 008 (16/16) a 086 (2/16)
2. Llevar **12 bicis** de 118 (18/19) a 256 (0/21)
3. Llevar **11 bicis** de 113 (14/15) a 041 (2/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

736 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.252 | 0.061 |
| Persistencia 0/1 | 0.252 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
