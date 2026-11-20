# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 21:56 (hora de Ciudad de México).

## Último pronóstico: 19/11 21:56 a 22:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 115 Roma-Dinamarca | 0 / 26 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 11 | 1.00 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.99 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 12-20 |
| 117 Londres-Nápoles | 1 / 28 | 0.88 | 0.00 | 0-1 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.81 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.74 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.70 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 17 | 0.62 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (20/20) a 118 (0/19)
2. Llevar **10 bicis** de 555 (17/29) a 117 (1/28)
3. Llevar **11 bicis** de 255 (25/30) a 115 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

219 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.036 |
| Sin resincronizar | 0.291 | 0.097 |
| Persistencia | 0.330 | 0.067 |
| Persistencia 0/1 | 0.330 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
