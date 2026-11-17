# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 17:25 (hora de Ciudad de México).

## Último pronóstico: 17/11 17:25 a 18:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.01 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 24 | 0.99 | 0.00 | 0-1 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 23 | 0.99 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 1 / 26 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (17/17) a 010 (0/24)
2. Llevar **14 bicis** de 555 (17/30) a 115 (2/24)
3. Llevar **8 bicis** de 107-108 (9/50) a 031 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

58 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.027 |
| Sin resincronizar | 0.276 | 0.092 |
| Persistencia | 0.346 | 0.047 |
| Persistencia 0/1 | 0.346 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
