# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 16:50 (hora de Ciudad de México).

## Último pronóstico: 26/11 16:50 a 17:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

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
| 010 Reforma - Ramírez | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 0 / 9 | 0.98 | 0.04 | 0-7 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.96 | 19-29 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.95 | 18-21 |
| 270 De la República-Ponciano Arr | 0 / 8 | 0.86 | 0.68 | 5-8 |
| 119 Turín-Abraham González | 2 / 24 | 0.84 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 2 / 10 | 0.83 | 0.01 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.80 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 26 | 0.76 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 260 (19/21) a 010 (0/24)
2. Llevar **13 bicis** de 029 (29/29) a 119 (2/24)
3. Llevar **10 bicis** de 114 (18/22) a 003 (2/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

695 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
