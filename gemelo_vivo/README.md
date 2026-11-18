# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 19:19 (hora de Ciudad de México).

## Último pronóstico: 17/11 19:18 a 20:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.4 °C** · lluvia 0.1 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.75** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.09 | 0-6 |
| 116 Londres-Roma | 0 / 16 | 1.00 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 8 | 1.00 | 0.02 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 23 | 1.00 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 555 (29/29) a 003 (0/29)
2. Llevar **12 bicis** de 450 (16/27) a 116 (0/16)
3. Llevar **10 bicis** de 260 (15/17) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

66 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.142 | 0.026 |
| Sin resincronizar | 0.309 | 0.089 |
| Persistencia | 0.372 | 0.045 |
| Persistencia 0/1 | 0.372 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
