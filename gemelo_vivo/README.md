# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 18:31 (hora de Ciudad de México).

## Último pronóstico: 24/11 18:31 a 19:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.7 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.67** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 27 | 1.00 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.98 | 0.00 | 0-9 |
| 026 Reforma - Versalles | 0 / 13 | 0.97 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.96 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.96 | 0.00 | 0-10 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.94 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.90 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 22 | 0.90 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 2 / 14 | 0.83 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 029 (27/34) a 117 (0/27)
2. Llevar **12 bicis** de 555 (17/30) a 020 (1/21)
3. Llevar **17 bicis** de 098 (26/29) a 031 (3/35)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

560 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
