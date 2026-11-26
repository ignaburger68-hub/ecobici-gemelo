# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 16:22 (hora de Ciudad de México).

## Último pronóstico: 26/11 16:21 a 17:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · lluvia 0.6 mm/h · viento 6 km/h · día hábil

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
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 4 | 0.80 | 0.98 | 4-4 |
| 112 Av. Morelos-Abraham González | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.93 | 0.69 | 2-5 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.90 | 18-21 |
| 107-108 Tolsa-Balderas | 1 / 54 | 0.78 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 30 | 0.76 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.72 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (19/21) a 010 (0/25)
2. Llevar **6 bicis** de 113 (12/14) a 026 (0/11)
3. Llevar **7 bicis** de 115 (20/24) a 112 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

693 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.249 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
