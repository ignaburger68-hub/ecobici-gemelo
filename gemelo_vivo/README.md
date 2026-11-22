# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 18:48 (hora de Ciudad de México).

## Último pronóstico: 21/11 18:48 a 19:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.98 | 0.00 | 0-11 |
| 115 Roma-Dinamarca | 0 / 27 | 0.97 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 1 / 15 | 0.85 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 1 / 23 | 0.81 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.75 | 12-19 |
| 112 Av. Morelos-Abraham González | 2 / 22 | 0.70 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.68 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.66 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (18/19) a 041 (0/31)
2. Llevar **13 bicis** de 031 (26/34) a 010 (0/27)
3. Llevar **10 bicis** de 270 (26/29) a 115 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

348 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
