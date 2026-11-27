# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 11:48 (hora de Ciudad de México).

## Último pronóstico: 27/11 11:48 a 12:48

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
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 10-15 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.93 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 8 | 0.90 | 0.24 | 2-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.90 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.88 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.62 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 16 / 18 | 0.00 | 0.55 | 11-18 |
| 116 Londres-Roma | 2 / 22 | 0.49 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (15/15) a 041 (1/29)
2. Llevar **12 bicis** de 114 (21/23) a 255 (1/34)
3. Llevar **8 bicis** de 118 (16/18) a 259 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

746 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
