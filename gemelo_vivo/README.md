# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 17:44 (hora de Ciudad de México).

## Último pronóstico: 27/11 17:44 a 18:44

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.5 °C** · lluvia 0.5 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.67** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 1.00 | 28-31 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 14 | 0.98 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 24 / 25 | 0.00 | 0.74 | 21-25 |
| 115 Roma-Dinamarca | 3 / 22 | 0.61 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 27 | 0.52 | 0.00 | 1-7 |
| 117 Londres-Nápoles | 3 / 30 | 0.49 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 3 / 16 | 0.42 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 029 (31/31) a 010 (0/25)
2. Llevar **8 bicis** de 119 (24/25) a 026 (0/14)
3. Llevar **6 bicis** de 113 (12/15) a 012 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

771 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.036 |
| Sin resincronizar | 0.241 | 0.081 |
| Persistencia | 0.245 | 0.060 |
| Persistencia 0/1 | 0.245 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
