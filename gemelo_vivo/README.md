# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 15:54 (hora de Ciudad de México).

## Último pronóstico: 25/11 15:53 a 16:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.9 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 008 Reforma - General Prim | 0 / 10 | 0.99 | 0.01 | 0-6 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 9 | 0.98 | 0.01 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.98 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.97 | 0.01 | 0-6 |
| 029 Reforma - Bucareli | 0 / 29 | 0.92 | 0.00 | 1-12 |
| 085 Rosas Moreno - Sullivan | 2 / 13 | 0.77 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (25/32) a 270 (0/26)
2. Llevar **9 bicis** de 116 (20/23) a 086 (0/16)
3. Llevar **7 bicis** de 117 (19/31) a 003 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

620 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.241 | 0.080 |
| Persistencia | 0.264 | 0.060 |
| Persistencia 0/1 | 0.264 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
