# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 11:19 (hora de Ciudad de México).

## Último pronóstico: 27/11 11:19 a 12:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.8 °C** · lluvia 0.6 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.54** y las **devoluciones por 0.62** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.97 | 10-15 |
| 107-108 Tolsa-Balderas | 0 / 29 | 0.89 | 0.00 | 4-13 |
| 115 Roma-Dinamarca | 22 / 23 | 0.00 | 0.73 | 16-23 |
| 116 Londres-Roma | 1 / 21 | 0.65 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 3 / 26 | 0.42 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 8 / 11 | 0.01 | 0.37 | 5-11 |
| 118 Liverpool-Dinamarca | 14 / 17 | 0.00 | 0.33 | 11-17 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (15/15) a 041 (0/28)
2. Llevar **10 bicis** de 115 (22/23) a 112 (0/22)
3. Llevar **7 bicis** de 118 (14/17) a 116 (1/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

744 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.037 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.250 | 0.062 |
| Persistencia 0/1 | 0.250 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
