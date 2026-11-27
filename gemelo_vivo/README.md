# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 09:54 (hora de Ciudad de México).

## Último pronóstico: 27/11 09:54 a 10:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.4 °C** · lluvia 0.8 mm/h · viento 8 km/h · día hábil

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
| 012 Río Lerma - Villalongín | 15 / 15 | 0.00 | 0.99 | 12-15 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 6-11 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.96 | 11-16 |
| 107-108 Tolsa-Balderas | 0 / 30 | 0.87 | 0.00 | 3-11 |
| 118 Liverpool-Dinamarca | 16 / 19 | 0.00 | 0.87 | 17-19 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.66 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 23 / 30 | 0.00 | 0.65 | 25-30 |
| 113 General Prim-Versalles | 12 / 15 | 0.00 | 0.63 | 10-15 |
| 010 Reforma - Ramírez | 21 / 25 | 0.00 | 0.58 | 19-25 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 012 (15/15) a 256 (1/22)
2. Llevar **10 bicis** de 118 (16/19) a 086 (4/17)
3. Llevar **16 bicis** de 117 (23/30) a 003 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

738 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.251 | 0.061 |
| Persistencia 0/1 | 0.251 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
