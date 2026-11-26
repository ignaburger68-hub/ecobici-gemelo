# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 10:52 (hora de Ciudad de México).

## Último pronóstico: 26/11 10:52 a 11:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 28 / 28 | 0.00 | 0.99 | 24-28 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.92 | 0.95 | 2-2 |
| 555 Ribera de San Cosme - Insurg | 2 / 29 | 0.92 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 0 / 13 | 0.88 | 0.08 | 3-12 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (28/28) a 555 (2/29)
2. Llevar **11 bicis** de 260 (19/21) a 010 (0/25)
3. Llevar **9 bicis** de 114 (19/22) a 012 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

670 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.244 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
