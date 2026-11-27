# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 11:34 (hora de Ciudad de México).

## Último pronóstico: 27/11 11:33 a 12:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · lluvia 2.3 mm/h · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.52** y las **devoluciones por 0.60** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 10-15 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 1 | 0.94 | 0.94 | 1-1 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.88 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.84 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 10 | 0.77 | 0.29 | 4-10 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 25 | 0.72 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 21 / 23 | 0.00 | 0.47 | 18-23 |
| 003 Reforma - Insurgentes | 3 / 29 | 0.45 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (15/15) a 041 (1/28)
2. Llevar **11 bicis** de 114 (21/23) a 112 (1/22)
3. Llevar **7 bicis** de 118 (14/17) a 086 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

745 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
