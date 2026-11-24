# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 14:28 (hora de Ciudad de México).

## Último pronóstico: 24/11 14:28 a 15:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · lluvia 0.4 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.68** y las **devoluciones por 0.72** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.98 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 1 / 55 | 0.96 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.94 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 15 / 15 | 0.01 | 0.94 | 5-14 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.90 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 5 / 26 | 0.83 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (18/22) a 270 (0/27)
2. Llevar **11 bicis** de 114 (19/20) a 107-108 (1/55)
3. Llevar **7 bicis** de 113 (15/15) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

543 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.084 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
