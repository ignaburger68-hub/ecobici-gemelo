# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 18:02 (hora de Ciudad de México).

## Último pronóstico: 24/11 18:02 a 19:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.4 °C** · lluvia 0.8 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 1.00 | 12-19 |
| 117 Londres-Nápoles | 1 / 27 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 5 / 33 | 0.93 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 22 | 0.92 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 1 / 12 | 0.92 | 0.02 | 0-7 |
| 012 Río Lerma - Villalongín | 2 / 12 | 0.91 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 15 / 15 | 0.02 | 0.88 | 5-14 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.80 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.77 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (19/19) a 117 (1/27)
2. Llevar **20 bicis** de 098 (27/29) a 031 (5/33)
3. Llevar **13 bicis** de 116 (22/23) a 020 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

558 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
