# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 12:31 (hora de Ciudad de México).

## Último pronóstico: 27/11 12:31 a 13:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.3 °C** · lluvia 5.5 mm/h · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.53** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | fuerte (≥4 mm/h) | 1.000 | 1.000 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.91 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 2 / 31 | 0.89 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.86 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.79 | 10-15 |
| 255 José Rosas Moreno-Guillermo  | 2 / 34 | 0.72 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 10 / 12 | 0.00 | 0.68 | 6-12 |
| 114 Lucerna-Abraham González | 21 / 23 | 0.00 | 0.63 | 18-23 |
| 118 Liverpool-Dinamarca | 16 / 17 | 0.00 | 0.59 | 10-17 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.45 | 9-15 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 114 (21/23) a 555 (2/31)
2. Llevar **8 bicis** de 113 (14/15) a 256 (1/21)
3. Llevar **6 bicis** de 012 (10/12) a 041 (1/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

749 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
