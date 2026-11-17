# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 17:53 (hora de Ciudad de México).

## Último pronóstico: 17/11 17:53 a 18:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.6 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.01 | 0-4 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 1 / 26 | 1.00 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.18 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 1 / 27 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.99 | 0.01 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.97 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 555 (23/30) a 031 (1/26)
2. Llevar **14 bicis** de 260 (17/18) a 117 (0/30)
3. Llevar **11 bicis** de 107-108 (15/49) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

60 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.027 |
| Sin resincronizar | 0.284 | 0.091 |
| Persistencia | 0.353 | 0.046 |
| Persistencia 0/1 | 0.353 | 0.046 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
