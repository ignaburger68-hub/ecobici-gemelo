# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 16:40 (hora de Ciudad de México).

## Último pronóstico: 21/11 16:40 a 17:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.3 °C** · sin lluvia · viento 6 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.98 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.87 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.85 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.84 | 0.00 | 0-4 |
| 116 Londres-Roma | 1 / 23 | 0.81 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 15 | 0.76 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.70 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 2 / 15 | 0.66 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 031 (30/34) a 115 (0/25)
2. Llevar **13 bicis** de 259 (22/25) a 041 (2/31)
3. Llevar **9 bicis** de 114 (16/21) a 085 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

339 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
