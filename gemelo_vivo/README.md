# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 22:43 (hora de Ciudad de México).

## Último pronóstico: 27/11 22:43 a 23:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**7.5 °C** · lluvia 2.3 mm/h · viento 9 km/h · día hábil

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
| 026 Reforma - Versalles | 0 / 14 | 1.00 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 012 Río Lerma - Villalongín | 0 / 11 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.97 | 13-16 |
| 041 Reforma - Av. de la Repúblic | 2 / 28 | 0.19 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 2 / 16 | 0.13 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 20 / 23 | 0.00 | 0.10 | 18-22 |
| 048 Independencia - Azueta | 5 / 10 | 0.02 | 0.00 | 2-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (16/16) a 026 (0/14)
2. Llevar **6 bicis** de 256 (20/23) a 010 (0/27)
3. Llevar **6 bicis** de 107-108 (49/56) a 117 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

792 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.110 | 0.036 |
| Sin resincronizar | 0.236 | 0.082 |
| Persistencia | 0.239 | 0.059 |
| Persistencia 0/1 | 0.239 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
