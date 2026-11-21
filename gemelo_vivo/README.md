# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 10:01 (hora de Ciudad de México).

## Último pronóstico: 21/11 10:01 a 11:01

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 29 | 0.98 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 30 / 31 | 0.00 | 0.79 | 23-31 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.51 | 0.00 | 1-16 |
| 115 Roma-Dinamarca | 2 / 27 | 0.48 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.48 | 0.00 | 0-8 |
| 012 Río Lerma - Villalongín | 12 / 15 | 0.00 | 0.47 | 9-15 |
| 085 Rosas Moreno - Sullivan | 3 / 15 | 0.44 | 0.00 | 0-6 |
| 116 Londres-Roma | 5 / 23 | 0.32 | 0.00 | 0-9 |
| 020 Reforma- Río Támesis | 4 / 23 | 0.31 | 0.00 | 1-12 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (30/31) a 119 (0/29)
2. Llevar **7 bicis** de 012 (12/15) a 112 (0/22)
3. Llevar **9 bicis** de 450 (27/30) a 041 (3/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

311 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
