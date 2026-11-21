# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 15:57 (hora de Ciudad de México).

## Último pronóstico: 21/11 15:57 a 16:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.2 °C** · sin lluvia · viento 10 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.88 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.86 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.73 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.64 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 3 / 27 | 0.62 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 2 / 15 | 0.62 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 26 | 0.00 | 0.49 | 21-26 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 259 (24/26) a 041 (2/31)
2. Llevar **9 bicis** de 270 (21/30) a 012 (0/14)
3. Llevar **12 bicis** de 555 (27/34) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

336 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
