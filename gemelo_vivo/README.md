# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 17:04 (hora de Ciudad de México).

## Último pronóstico: 26/11 17:04 a 18:04

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
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 18-21 |
| 026 Reforma - Versalles | 0 / 11 | 1.00 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.95 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.91 | 23-29 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.86 | 0.88 | 5-6 |
| 119 Turín-Abraham González | 3 / 24 | 0.86 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 3 / 22 | 0.82 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 260 (21/21) a 010 (0/25)
2. Llevar **10 bicis** de 029 (29/29) a 026 (0/11)
3. Llevar **10 bicis** de 114 (21/22) a 085 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

696 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
