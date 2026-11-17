# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 15:44 (hora de Ciudad de México).

## Último pronóstico: 17/11 15:44 a 16:44

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
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 029 Reforma - Bucareli | 0 / 32 | 0.98 | 0.00 | 0-9 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.96 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 24 | 0.96 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.89 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 17 | 0.87 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.86 | 0.20 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 117 (22/30) a 010 (0/27)
2. Llevar **8 bicis** de 098 (12/30) a 259 (0/24)
3. Llevar **7 bicis** de 031 (14/26) a 029 (0/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

51 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.149 | 0.029 |
| Sin resincronizar | 0.244 | 0.094 |
| Persistencia | 0.320 | 0.054 |
| Persistencia 0/1 | 0.320 | 0.054 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
