# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 16:27 (hora de Ciudad de México).

## Último pronóstico: 17/11 16:26 a 17:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 0 / 17 | 0.97 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 27 | 0.90 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.89 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 2 / 16 | 0.79 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.79 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 23 | 0.76 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 1 / 24 | 0.74 | 0.00 | 1-11 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 031 (16/26) a 010 (1/27)
2. Llevar **6 bicis** de 119 (11/24) a 270 (0/24)
3. Llevar **6 bicis** de 117 (18/30) a 113 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

54 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.028 |
| Sin resincronizar | 0.258 | 0.093 |
| Persistencia | 0.330 | 0.050 |
| Persistencia 0/1 | 0.330 | 0.050 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
