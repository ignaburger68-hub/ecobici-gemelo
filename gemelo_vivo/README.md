# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 09:43 (hora de Ciudad de México).

## Último pronóstico: 19/11 09:43 a 10:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 14 / 14 | 0.00 | 0.99 | 11-14 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 1-8 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.99 | 11-13 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.98 | 0.00 | 2-14 |
| 114 Lucerna-Abraham González | 17 / 18 | 0.00 | 0.94 | 12-18 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.92 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 114 (17/18) a 107-108 (0/55)
2. Llevar **9 bicis** de 113 (13/13) a 260 (0/20)
3. Llevar **9 bicis** de 008 (14/14) a 256 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

168 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.036 |
| Sin resincronizar | 0.279 | 0.089 |
| Persistencia | 0.332 | 0.068 |
| Persistencia 0/1 | 0.332 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
