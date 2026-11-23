# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 11:27 (hora de Ciudad de México).

## Último pronóstico: 23/11 11:26 a 12:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.90** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 14 / 14 | 0.00 | 0.98 | 10-14 |
| 118 Liverpool-Dinamarca | 17 / 18 | 0.00 | 0.88 | 15-18 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.82 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 2 / 28 | 0.67 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.62 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 2 / 16 | 0.52 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.50 | 0.00 | 1-11 |
| 048 Independencia - Azueta | 1 / 11 | 0.45 | 0.04 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (17/18) a 255 (1/34)
2. Llevar **8 bicis** de 026 (14/14) a 270 (2/28)
3. Llevar **9 bicis** de 115 (21/25) a 263 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

459 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.254 | 0.088 |
| Persistencia | 0.293 | 0.064 |
| Persistencia 0/1 | 0.293 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
