# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 14:25 (hora de Ciudad de México).

## Último pronóstico: 27/11 14:25 a 15:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.8 °C** · lluvia 0.3 mm/h · viento 13 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 0 / 12 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.02 | 0.98 | 4-13 |
| 048 Independencia - Azueta | 2 / 10 | 0.90 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 14 | 0.89 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.87 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 3 / 21 | 0.87 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 25 | 0.85 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (15/15) a 086 (0/15)
2. Llevar **13 bicis** de 107-108 (36/55) a 115 (6/23)
3. Llevar **8 bicis** de 114 (20/23) a 012 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

757 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.037 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.248 | 0.061 |
| Persistencia 0/1 | 0.248 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
