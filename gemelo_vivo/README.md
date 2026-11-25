# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 14:28 (hora de Ciudad de México).

## Último pronóstico: 25/11 14:28 a 15:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.95 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.86 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.80 | 0.01 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.79 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.76 | 0.01 | 1-10 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.75 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.74 | 0.00 | 0-8 |
| 041 Reforma - Av. de la Repúblic | 2 / 30 | 0.72 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 2 / 18 | 0.71 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 031 (29/33) a 270 (1/25)
2. Llevar **7 bicis** de 116 (20/23) a 012 (1/13)
3. Llevar **6 bicis** de 026 (10/12) a 256 (3/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

614 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.263 | 0.060 |
| Persistencia 0/1 | 0.263 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
