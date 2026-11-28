# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 20:20 (hora de Ciudad de México).

## Último pronóstico: 27/11 20:20 a 21:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.1 °C** · lluvia 1.3 mm/h · viento 9 km/h · día hábil

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
| 041 Reforma - Av. de la Repúblic | 0 / 27 | 0.98 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 15 / 16 | 0.00 | 0.68 | 11-16 |
| 010 Reforma - Ramírez | 2 / 26 | 0.67 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 2 / 28 | 0.52 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 25 | 0.50 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 2 / 14 | 0.43 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 2 / 11 | 0.42 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 2 / 16 | 0.30 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 5 / 32 | 0.24 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (15/16) a 041 (0/27)
2. Llevar **9 bicis** de 256 (17/22) a 010 (2/26)
3. Llevar **8 bicis** de 119 (19/26) a 117 (2/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

782 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.239 | 0.082 |
| Persistencia | 0.242 | 0.060 |
| Persistencia 0/1 | 0.242 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
