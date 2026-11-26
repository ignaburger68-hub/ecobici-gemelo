# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 16:36 (hora de Ciudad de México).

## Último pronóstico: 26/11 16:36 a 17:36

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
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 9 | 0.96 | 0.03 | 0-6 |
| 029 Reforma - Bucareli | 29 / 30 | 0.00 | 0.92 | 18-29 |
| 270 De la República-Ponciano Arr | 0 / 9 | 0.91 | 0.29 | 3-9 |
| 010 Reforma - Ramírez | 2 / 24 | 0.90 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.90 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 18 / 21 | 0.00 | 0.82 | 17-21 |
| 112 Av. Morelos-Abraham González | 1 / 14 | 0.80 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 1 / 26 | 0.69 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (18/21) a 010 (2/24)
2. Llevar **8 bicis** de 029 (29/30) a 026 (0/11)
3. Llevar **11 bicis** de 114 (17/22) a 003 (1/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

694 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
