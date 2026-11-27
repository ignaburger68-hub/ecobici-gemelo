# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 21:21 (hora de Ciudad de México).

## Último pronóstico: 26/11 21:21 a 22:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.8 °C** · lluvia 0.3 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.86 | 0.93 | 3-3 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.85 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 3 / 28 | 0.83 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 8 / 9 | 0.00 | 0.78 | 6-9 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.78 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 11 | 0.73 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 2 / 13 | 0.67 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 2 / 10 | 0.64 | 0.01 | 0-5 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 029 (26/29) a 010 (0/26)
2. Llevar **6 bicis** de 048 (8/9) a 117 (3/28)
3. Llevar **9 bicis** de 041 (21/27) a 012 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

714 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.037 |
| Sin resincronizar | 0.248 | 0.082 |
| Persistencia | 0.257 | 0.062 |
| Persistencia 0/1 | 0.257 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
