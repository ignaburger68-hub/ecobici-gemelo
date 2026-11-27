# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 12:17 (hora de Ciudad de México).

## Último pronóstico: 27/11 12:17 a 13:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · lluvia 2.3 mm/h · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.50** y las **devoluciones por 0.58** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 17 / 17 | 0.00 | 0.97 | 10-17 |
| 026 Reforma - Versalles | 15 / 15 | 0.00 | 0.96 | 10-15 |
| 555 Ribera de San Cosme - Insurg | 2 / 32 | 0.88 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.79 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.76 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 2 / 21 | 0.74 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.72 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.70 | 10-15 |
| 114 Lucerna-Abraham González | 21 / 23 | 0.00 | 0.61 | 18-23 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 114 (21/23) a 555 (2/32)
2. Llevar **7 bicis** de 118 (17/17) a 256 (2/21)
3. Llevar **7 bicis** de 026 (15/15) a 255 (1/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

748 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.037 |
| Sin resincronizar | 0.242 | 0.081 |
| Persistencia | 0.249 | 0.062 |
| Persistencia 0/1 | 0.249 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
