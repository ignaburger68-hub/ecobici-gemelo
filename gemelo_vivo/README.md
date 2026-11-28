# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 19:23 (hora de Ciudad de México).

## Último pronóstico: 27/11 19:23 a 20:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.3 °C** · lluvia 1.3 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.56** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.98 | 20-23 |
| 008 Reforma - General Prim | 0 / 15 | 0.98 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 23 | 0.98 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 25 | 0.96 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 14 / 15 | 0.00 | 0.76 | 11-15 |
| 026 Reforma - Versalles | 1 / 14 | 0.73 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 28 / 30 | 0.00 | 0.59 | 25-30 |
| 119 Turín-Abraham González | 23 / 25 | 0.00 | 0.30 | 20-25 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (14/15) a 115 (0/23)
2. Llevar **6 bicis** de 114 (23/23) a 012 (0/11)
3. Llevar **9 bicis** de 029 (28/30) a 010 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

778 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.239 | 0.082 |
| Persistencia | 0.243 | 0.060 |
| Persistencia 0/1 | 0.243 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
