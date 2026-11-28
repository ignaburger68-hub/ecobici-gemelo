# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 20:34 (hora de Ciudad de México).

## Último pronóstico: 27/11 20:34 a 21:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.1 °C** · lluvia 1.5 mm/h · viento 7 km/h · día hábil

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
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.99 | 11-16 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.77 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.75 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 2 / 26 | 0.72 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 2 / 28 | 0.56 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 2 / 14 | 0.42 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 6 / 32 | 0.32 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 2 / 16 | 0.24 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 4 / 26 | 0.20 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (16/16) a 010 (2/26)
2. Llevar **10 bicis** de 107-108 (45/56) a 041 (1/28)
3. Llevar **6 bicis** de 256 (17/22) a 012 (1/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

783 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.238 | 0.082 |
| Persistencia | 0.242 | 0.060 |
| Persistencia 0/1 | 0.242 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
