# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 20:09 (hora de Ciudad de México).

## Último pronóstico: 26/11 20:09 a 21:09

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.98 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.79 | 0.97 | 3-3 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.95 | 23-29 |
| 113 General Prim-Versalles | 0 / 13 | 0.93 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.92 | 16-20 |
| 256 Gómez Farías-Sadi Carnot | 19 / 20 | 0.00 | 0.79 | 14-20 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.72 | 0.02 | 0-10 |
| 041 Reforma - Av. de la Repúblic | 26 / 28 | 0.00 | 0.65 | 20-28 |
| 010 Reforma - Ramírez | 4 / 26 | 0.60 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 260 (19/20) a 012 (0/14)
2. Llevar **13 bicis** de 029 (29/29) a 010 (4/26)
3. Llevar **6 bicis** de 256 (19/20) a 113 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

709 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.249 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
