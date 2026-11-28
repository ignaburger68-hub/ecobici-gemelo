# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 22:28 (hora de Ciudad de México).

## Último pronóstico: 27/11 22:28 a 23:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**7.9 °C** · lluvia 2.5 mm/h · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.56** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 0 / 14 | 0.99 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.99 | 13-16 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 1 / 27 | 0.56 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.40 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 16 | 0.15 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 20 / 23 | 0.00 | 0.10 | 18-22 |
| 115 Roma-Dinamarca | 4 / 26 | 0.04 | 0.00 | 2-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 086 (16/16) a 026 (0/14)
2. Llevar **11 bicis** de 256 (20/23) a 117 (0/28)
3. Llevar **5 bicis** de 107-108 (49/56) a 012 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

791 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.110 | 0.036 |
| Sin resincronizar | 0.236 | 0.082 |
| Persistencia | 0.240 | 0.059 |
| Persistencia 0/1 | 0.240 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
