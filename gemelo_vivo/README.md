# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 21:42 (hora de Ciudad de México).

## Último pronóstico: 19/11 21:42 a 22:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 14-20 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.97 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 1 / 26 | 0.84 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 1 / 28 | 0.82 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.74 | 0.00 | 0-3 |
| 116 Londres-Roma | 1 / 20 | 0.73 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.72 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 2 / 19 | 0.67 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 17 | 0.60 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 260 (20/20) a 117 (1/28)
2. Llevar **12 bicis** de 555 (17/29) a 115 (1/26)
3. Llevar **6 bicis** de 026 (13/15) a 116 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

218 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
