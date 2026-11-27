# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 19:26 (hora de Ciudad de México).

## Último pronóstico: 26/11 19:26 a 20:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

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
| 555 Ribera de San Cosme - Insurg | 35 / 35 | 0.00 | 1.00 | 29-35 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 1.00 | 5-10 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.99 | 26-33 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.76 | 0.98 | 5-5 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.95 | 0.04 | 1-11 |
| 115 Roma-Dinamarca | 0 / 24 | 0.94 | 0.00 | 0-10 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.81 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 27 / 30 | 0.00 | 0.77 | 24-30 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.76 | 16-22 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 555 (35/35) a 115 (0/24)
2. Llevar **13 bicis** de 029 (33/33) a 114 (1/21)
3. Llevar **7 bicis** de 048 (10/10) a 086 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

706 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
