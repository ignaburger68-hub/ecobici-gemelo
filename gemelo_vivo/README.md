# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 01:40 (hora de Ciudad de México).

## Último pronóstico: 24/11 22:50 a 23:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · lluvia 1.0 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.55** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 25 | 1.00 | 0.00 | 0-1 |
| 118 Liverpool-Dinamarca | 0 / 18 | 1.00 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 28 / 28 | 0.00 | 0.99 | 26-28 |
| 098 Emilio Dondé-Av. Balderas | 31 / 31 | 0.00 | 0.99 | 28-31 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.75 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.68 | 0.00 | 0-3 |
| 116 Londres-Roma | 2 / 23 | 0.59 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.53 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.43 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 27 / 29 | 0.00 | 0.39 | 22-29 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (28/28) a 115 (0/25)
2. Llevar **7 bicis** de 098 (31/31) a 086 (1/14)
3. Llevar **9 bicis** de 555 (27/29) a 118 (0/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

582 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.239 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
