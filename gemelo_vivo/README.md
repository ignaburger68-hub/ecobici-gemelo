# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 14:11 (hora de Ciudad de México).

## Último pronóstico: 27/11 14:10 a 15:10

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
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 10 | 0.98 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 3 / 21 | 0.93 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 2 / 12 | 0.91 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.86 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 28 | 0.84 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 107-108 (39/55) a 010 (0/25)
2. Llevar **9 bicis** de 113 (13/15) a 256 (3/21)
3. Llevar **9 bicis** de 107-108 (39/55) a 255 (0/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

756 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
