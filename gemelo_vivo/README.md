# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 18:41 (hora de Ciudad de México).

## Último pronóstico: 27/11 18:41 a 19:41

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**8.3 °C** · lluvia 1.3 mm/h · viento 10 km/h · día hábil

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
| 026 Reforma - Versalles | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.84 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 1 / 25 | 0.81 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 28 / 30 | 0.00 | 0.75 | 26-30 |
| 008 Reforma - General Prim | 2 / 16 | 0.69 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 22 | 0.60 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 3 / 30 | 0.58 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 2 / 17 | 0.46 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 27 | 0.40 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 029 (28/30) a 012 (1/11)
2. Llevar **11 bicis** de 119 (23/25) a 010 (1/25)
3. Llevar **4 bicis** de 048 (7/10) a 026 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

775 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.240 | 0.082 |
| Persistencia | 0.244 | 0.060 |
| Persistencia 0/1 | 0.244 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
