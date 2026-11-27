# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 12:02 (hora de Ciudad de México).

## Último pronóstico: 27/11 12:02 a 13:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · lluvia 2.3 mm/h · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.47** y las **devoluciones por 0.56** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.99 | 11-15 |
| 118 Liverpool-Dinamarca | 18 / 18 | 0.00 | 0.98 | 12-18 |
| 026 Reforma - Versalles | 15 / 15 | 0.00 | 0.96 | 10-15 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.78 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.63 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 4 / 32 | 0.59 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 10 / 12 | 0.00 | 0.50 | 7-12 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (15/15) a 041 (0/29)
2. Llevar **9 bicis** de 118 (18/18) a 555 (4/32)
3. Llevar **6 bicis** de 026 (15/15) a 112 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

747 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.037 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.249 | 0.062 |
| Persistencia 0/1 | 0.249 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
