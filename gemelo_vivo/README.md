# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 21:07 (hora de Ciudad de México).

## Último pronóstico: 26/11 21:07 a 22:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.8 °C** · lluvia 0.3 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

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
| 048 Independencia - Azueta | 9 / 9 | 0.00 | 0.98 | 6-9 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.81 | 0.98 | 3-3 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.94 | 22-29 |
| 026 Reforma - Versalles | 2 / 13 | 0.81 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 11 | 0.75 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 2 / 14 | 0.73 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 5 / 28 | 0.69 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 13 | 0.68 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 029 (29/29) a 010 (0/26)
2. Llevar **7 bicis** de 048 (9/9) a 117 (5/28)
3. Llevar **8 bicis** de 041 (25/28) a 026 (2/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

713 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
