# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 10:00 (hora de Ciudad de México).

## Último pronóstico: 17/11 10:00 a 11:00

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
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 6 | 0.99 | 0.04 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.98 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 0.97 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.97 | 12-16 |
| 010 Reforma - Ramírez | 0 / 27 | 0.96 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 1 / 10 | 0.96 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.88 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.85 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 008 (16/16) a 270 (0/25)
2. Llevar **7 bicis** de 555 (14/31) a 048 (1/10)
3. Llevar **10 bicis** de 107-108 (16/54) a 098 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

27 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.141 | 0.045 |
| Sin resincronizar | 0.156 | 0.077 |
| Persistencia | 0.324 | 0.104 |
| Persistencia 0/1 | 0.324 | 0.104 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
