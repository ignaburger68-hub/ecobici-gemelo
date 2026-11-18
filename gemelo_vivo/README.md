# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 20:44 (hora de Ciudad de México).

## Último pronóstico: 17/11 20:44 a 21:44

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.1 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 4 | 1.00 | 0.32 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 16 | 0.99 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 10 | 0.98 | 0.03 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.96 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 2 / 26 | 0.95 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 2 / 20 | 0.90 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 450 (26/27) a 010 (2/26)
2. Llevar **12 bicis** de 555 (28/29) a 003 (1/31)
3. Llevar **13 bicis** de 259 (18/24) a 041 (2/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

72 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.132 | 0.028 |
| Sin resincronizar | 0.320 | 0.091 |
| Persistencia | 0.370 | 0.048 |
| Persistencia 0/1 | 0.370 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
