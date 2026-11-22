# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 19:16 (hora de Ciudad de México).

## Último pronóstico: 21/11 19:16 a 20:16

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
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.99 | 14-19 |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.96 | 0.00 | 0-8 |
| 115 Roma-Dinamarca | 0 / 27 | 0.94 | 0.00 | 0-9 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.67 | 0.00 | 1-14 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.66 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 1 / 15 | 0.56 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 2 / 16 | 0.56 | 0.00 | 0-8 |
| 450 Ramos Arizpe- Av México Teno | 28 / 30 | 0.00 | 0.47 | 25-30 |
| 086 Sullivan-Insurgentes | 3 / 14 | 0.44 | 0.01 | 0-8 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (19/19) a 003 (0/28)
2. Llevar **14 bicis** de 031 (24/34) a 010 (0/27)
3. Llevar **11 bicis** de 450 (28/30) a 115 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

350 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
