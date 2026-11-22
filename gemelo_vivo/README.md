# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 08:04 (hora de Ciudad de México).

## Último pronóstico: 22/11 08:03 a 09:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.8 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 15 | 0.98 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.79 | 0.00 | 0-4 |
| 116 Londres-Roma | 1 / 22 | 0.71 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.59 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 2 / 11 | 0.58 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.52 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 27 | 0.48 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 17 | 0.47 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 26 | 0.40 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 3 / 30 | 0.33 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 259 (24/26) a 041 (2/31)
2. Llevar **8 bicis** de 270 (22/29) a 026 (0/15)
3. Llevar **9 bicis** de 107-108 (19/58) a 116 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

374 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
