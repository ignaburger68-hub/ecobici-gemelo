# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 15:35 (hora de Ciudad de México).

## Último pronóstico: 27/11 15:35 a 16:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.4 °C** · lluvia 0.5 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.99 | 13-15 |
| 012 Río Lerma - Villalongín | 0 / 12 | 0.98 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.53 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 21 / 23 | 0.00 | 0.47 | 20-23 |
| 010 Reforma - Ramírez | 3 / 25 | 0.41 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.32 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 3 / 14 | 0.29 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 3 / 16 | 0.14 | 0.00 | 1-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 113 (15/15) a 003 (0/27)
2. Llevar **6 bicis** de 114 (21/23) a 012 (0/12)
3. Llevar **10 bicis** de 029 (24/30) a 010 (3/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

762 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.248 | 0.061 |
| Persistencia 0/1 | 0.248 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
