# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 16:46 (hora de Ciudad de México).

## Último pronóstico: 27/11 16:46 a 17:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.3 °C** · lluvia 0.4 mm/h · viento 6 km/h · día hábil

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
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 0.99 | 27-31 |
| 012 Río Lerma - Villalongín | 0 / 12 | 0.98 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.97 | 0.01 | 0-5 |
| 010 Reforma - Ramírez | 2 / 25 | 0.68 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 22 / 23 | 0.00 | 0.66 | 19-23 |
| 117 Londres-Nápoles | 4 / 30 | 0.46 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 2 / 14 | 0.45 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 27 | 0.42 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 13 / 15 | 0.00 | 0.38 | 10-15 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 029 (31/31) a 012 (0/12)
2. Llevar **9 bicis** de 114 (22/23) a 010 (2/25)
3. Llevar **4 bicis** de 113 (13/15) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

767 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.242 | 0.081 |
| Persistencia | 0.246 | 0.060 |
| Persistencia 0/1 | 0.246 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
