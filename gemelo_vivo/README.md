# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 13:14 (hora de Ciudad de México).

## Último pronóstico: 26/11 13:14 a 14:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

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
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 21 / 21 | 0.00 | 0.98 | 16-21 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.97 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.96 | 19-27 |
| 270 De la República-Ponciano Arr | 0 / 9 | 0.93 | 0.21 | 2-9 |
| 029 Reforma - Bucareli | 0 / 9 | 0.89 | 0.18 | 2-9 |
| 255 José Rosas Moreno-Guillermo  | 1 / 32 | 0.88 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.85 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.79 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 114 (21/21) a 041 (1/32)
2. Llevar **8 bicis** de 117 (27/27) a 085 (0/13)
3. Llevar **7 bicis** de 113 (13/14) a 086 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

680 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.246 | 0.081 |
| Persistencia | 0.259 | 0.060 |
| Persistencia 0/1 | 0.259 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
