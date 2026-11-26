# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 15:07 (hora de Ciudad de México).

## Último pronóstico: 26/11 15:07 a 16:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 008 Reforma - General Prim | 0 / 12 | 1.00 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 1 / 25 | 0.98 | 0.00 | 0-2 |
| 029 Reforma - Bucareli | 0 / 3 | 0.90 | 0.96 | 3-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 33 | 0.94 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 1 / 8 | 0.92 | 0.02 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.91 | 0.55 | 3-6 |
| 041 Reforma - Av. de la Repúblic | 2 / 32 | 0.84 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.84 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.83 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (27/28) a 010 (1/25)
2. Llevar **13 bicis** de 114 (20/22) a 555 (1/33)
3. Llevar **8 bicis** de 260 (19/21) a 008 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

688 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.248 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
