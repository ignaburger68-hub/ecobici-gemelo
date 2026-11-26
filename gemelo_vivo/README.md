# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 10:38 (hora de Ciudad de México).

## Último pronóstico: 26/11 10:38 a 11:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.99 | 23-27 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 9-15 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 27 | 0.98 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.93 | 0.82 | 2-3 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (27/27) a 555 (0/27)
2. Llevar **10 bicis** de 113 (15/15) a 107-108 (0/54)
3. Llevar **10 bicis** de 260 (19/21) a 256 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

669 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
