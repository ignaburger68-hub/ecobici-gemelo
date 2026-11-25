# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 18:17 (hora de Ciudad de México).

## Último pronóstico: 24/11 18:16 a 19:16

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
| 117 Londres-Nápoles | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 1-12 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.99 | 11-19 |
| 026 Reforma - Versalles | 0 / 12 | 0.98 | 0.02 | 0-7 |
| 115 Roma-Dinamarca | 1 / 26 | 0.96 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 6 / 35 | 0.93 | 0.00 | 0-8 |
| 010 Reforma - Ramírez | 1 / 21 | 0.93 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.90 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 53 | 0.85 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (18/19) a 117 (0/27)
2. Llevar **16 bicis** de 029 (21/34) a 031 (6/35)
3. Llevar **11 bicis** de 116 (20/23) a 118 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

559 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
