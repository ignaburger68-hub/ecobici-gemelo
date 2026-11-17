# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 10:14 (hora de Ciudad de México).

## Último pronóstico: 17/11 10:14 a 11:14

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**15.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.02 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.97 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 27 | 0.96 | 0.00 | 0-7 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.91 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 2 / 10 | 0.88 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 25 | 0.76 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.71 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 15 / 16 | 0.00 | 0.67 | 11-16 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 008 (15/16) a 098 (1/30)
2. Llevar **5 bicis** de 113 (7/10) a 048 (2/10)
3. Llevar **5 bicis** de 107-108 (14/54) a 086 (0/7)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

28 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.043 |
| Sin resincronizar | 0.164 | 0.079 |
| Persistencia | 0.317 | 0.099 |
| Persistencia 0/1 | 0.317 | 0.099 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
