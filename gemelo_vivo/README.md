# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 17:20 (hora de Ciudad de México).

## Último pronóstico: 24/11 17:20 a 18:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.7 °C** · lluvia 1.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.55** y las **devoluciones por 0.62** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 21 | 0.97 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.97 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 12 / 13 | 0.00 | 0.96 | 6-13 |
| 008 Reforma - General Prim | 16 / 16 | 0.01 | 0.94 | 7-15 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.88 | 0.01 | 0-5 |
| 260 Av. Juárez-Balderas | 14 / 19 | 0.00 | 0.85 | 14-19 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.84 | 0.00 | 1-13 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.84 | 0.00 | 1-9 |
| 026 Reforma - Versalles | 1 / 12 | 0.82 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 23 | 0.75 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (14/19) a 010 (0/21)
2. Llevar **9 bicis** de 086 (12/13) a 270 (0/27)
3. Llevar **7 bicis** de 098 (25/29) a 012 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

555 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
