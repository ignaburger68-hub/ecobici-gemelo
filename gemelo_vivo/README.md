# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 18:55 (hora de Ciudad de México).

## Último pronóstico: 27/11 18:55 a 19:55

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
| 029 Reforma - Bucareli | 30 / 30 | 0.00 | 1.00 | 27-30 |
| 012 Río Lerma - Villalongín | 0 / 11 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 22 | 0.98 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 25 | 0.81 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 14 | 0.67 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 16 | 0.65 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 24 / 25 | 0.00 | 0.64 | 19-25 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.63 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 7 / 10 | 0.00 | 0.39 | 5-10 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (30/30) a 115 (0/22)
2. Llevar **7 bicis** de 119 (24/25) a 012 (0/11)
3. Llevar **5 bicis** de 048 (7/10) a 010 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

776 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.111 | 0.036 |
| Sin resincronizar | 0.240 | 0.082 |
| Persistencia | 0.244 | 0.060 |
| Persistencia 0/1 | 0.244 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
