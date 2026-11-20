# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 03:08 (hora de Ciudad de México).

## Último pronóstico: 19/11 22:53 a 23:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 116 Londres-Roma | 1 / 20 | 0.83 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.79 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 1 / 36 | 0.79 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 17 | 0.69 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 4 / 28 | 0.64 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 260 (18/20) a 115 (0/25)
2. Llevar **16 bicis** de 259 (20/25) a 263 (4/28)
3. Llevar **10 bicis** de 555 (17/26) a 020 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

227 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.289 | 0.095 |
| Persistencia | 0.326 | 0.064 |
| Persistencia 0/1 | 0.326 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
