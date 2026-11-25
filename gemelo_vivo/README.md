# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 18:45 (hora de Ciudad de México).

## Último pronóstico: 24/11 18:45 a 19:45

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.7 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.62** y las **devoluciones por 0.69** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 27 | 1.00 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 0 / 13 | 1.00 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.96 | 0.00 | 1-7 |
| 115 Roma-Dinamarca | 1 / 26 | 0.95 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 13 | 0.93 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.93 | 0.00 | 0-10 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.93 | 11-19 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.93 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 1 / 35 | 0.93 | 0.00 | 0-7 |
| 118 Liverpool-Dinamarca | 3 / 18 | 0.91 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (20/30) a 086 (0/13)
2. Llevar **12 bicis** de 260 (19/19) a 117 (0/27)
3. Llevar **16 bicis** de 029 (25/33) a 115 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

561 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
