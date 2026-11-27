# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 16:18 (hora de Ciudad de México).

## Último pronóstico: 27/11 16:18 a 17:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.4 °C** · lluvia 0.5 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 14 | 0.98 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 12 | 0.98 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 29 / 31 | 0.00 | 0.72 | 26-31 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.68 | 11-15 |
| 041 Reforma - Av. de la Repúblic | 1 / 27 | 0.65 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 21 / 23 | 0.00 | 0.54 | 19-23 |
| 010 Reforma - Ramírez | 2 / 24 | 0.53 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 3 / 32 | 0.42 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (29/31) a 026 (0/14)
2. Llevar **6 bicis** de 113 (14/15) a 012 (0/12)
3. Llevar **5 bicis** de 114 (21/23) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

765 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.242 | 0.081 |
| Persistencia | 0.247 | 0.060 |
| Persistencia 0/1 | 0.247 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
