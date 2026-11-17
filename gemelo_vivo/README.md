# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 10:28 (hora de Ciudad de México).

## Último pronóstico: 17/11 10:28 a 11:28

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
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 27 | 0.97 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.85 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.84 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.80 | 0.04 | 0-4 |
| 048 Independencia - Azueta | 2 / 10 | 0.79 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 15 / 16 | 0.00 | 0.75 | 11-16 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 008 (15/16) a 098 (0/30)
2. Llevar **5 bicis** de 026 (8/10) a 255 (0/28)
3. Llevar **5 bicis** de 113 (8/10) a 270 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

29 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.153 | 0.040 |
| Sin resincronizar | 0.173 | 0.081 |
| Persistencia | 0.310 | 0.098 |
| Persistencia 0/1 | 0.310 | 0.098 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
