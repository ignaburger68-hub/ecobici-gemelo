# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 16:54 (hora de Ciudad de México).

## Último pronóstico: 21/11 16:54 a 17:54

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
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 33 / 33 | 0.00 | 0.95 | 24-32 |
| 026 Reforma - Versalles | 1 / 15 | 0.81 | 0.00 | 0-4 |
| 116 Londres-Roma | 1 / 22 | 0.80 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.77 | 0.01 | 0-7 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.75 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 2 / 27 | 0.66 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 2 / 14 | 0.65 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.64 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 031 (33/33) a 115 (0/26)
2. Llevar **9 bicis** de 259 (23/25) a 008 (0/15)
3. Llevar **8 bicis** de 270 (24/29) a 116 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

340 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
