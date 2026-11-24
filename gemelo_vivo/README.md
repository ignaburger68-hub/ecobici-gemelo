# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 17:34 (hora de Ciudad de México).

## Último pronóstico: 24/11 17:34 a 18:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.4 °C** · lluvia 0.8 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.63** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.99 | 17-19 |
| 026 Reforma - Versalles | 0 / 12 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.98 | 0.00 | 1-8 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 1 / 27 | 0.97 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 16 / 16 | 0.02 | 0.90 | 4-14 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.88 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.88 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 21 | 0.77 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 26 / 29 | 0.00 | 0.76 | 25-29 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 260 (18/19) a 117 (1/27)
2. Llevar **15 bicis** de 098 (26/29) a 270 (0/26)
3. Llevar **7 bicis** de 086 (11/14) a 026 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

556 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
