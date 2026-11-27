# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 19:40 (hora de Ciudad de México).

## Último pronóstico: 26/11 19:40 a 20:40

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
| 270 De la República-Ponciano Arr | 0 / 4 | 0.74 | 0.99 | 4-4 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.97 | 25-33 |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.92 | 0.01 | 0-8 |
| 041 Reforma - Av. de la Repúblic | 28 / 29 | 0.00 | 0.91 | 23-29 |
| 256 Gómez Farías-Sadi Carnot | 20 / 21 | 0.00 | 0.85 | 16-21 |
| 260 Av. Juárez-Balderas | 17 / 21 | 0.00 | 0.78 | 17-21 |
| 555 Ribera de San Cosme - Insurg | 26 / 32 | 0.00 | 0.77 | 25-32 |
| 048 Independencia - Azueta | 7 / 9 | 0.02 | 0.76 | 4-9 |
| 116 Londres-Roma | 21 / 23 | 0.00 | 0.70 | 15-23 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 555 (26/32) a 117 (1/29)
2. Llevar **11 bicis** de 041 (28/29) a 115 (1/23)
3. Llevar **8 bicis** de 029 (33/33) a 012 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

707 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
