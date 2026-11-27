# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 13:42 (hora de Ciudad de México).

## Último pronóstico: 27/11 13:42 a 14:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.3 °C** · lluvia 5.0 mm/h · viento 13 km/h · día hábil

El clima multiplica los **retiros por 0.59** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | fuerte (≥4 mm/h) | 1.000 | 1.000 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 32 | 0.98 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.96 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.92 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.90 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 14 | 0.85 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 107-108 (42/55) a 041 (0/28)
2. Llevar **13 bicis** de 114 (22/23) a 086 (0/15)
3. Llevar **9 bicis** de 113 (12/15) a 555 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

754 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.037 |
| Sin resincronizar | 0.242 | 0.081 |
| Persistencia | 0.248 | 0.061 |
| Persistencia 0/1 | 0.248 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
