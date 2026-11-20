# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 17:52 (hora de Ciudad de México).

## Último pronóstico: 20/11 17:52 a 18:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.2 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 1.00 | 27-33 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.99 | 16-20 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.98 | 13-22 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.82 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 4 / 21 | 0.77 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 7 / 23 | 0.73 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 4 / 13 | 0.70 | 0.01 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.65 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 5 / 15 | 0.63 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (20/20) a 115 (7/23)
2. Llevar **14 bicis** de 029 (33/33) a 020 (4/21)
3. Llevar **11 bicis** de 116 (22/22) a 256 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

273 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.270 | 0.094 |
| Persistencia | 0.307 | 0.067 |
| Persistencia 0/1 | 0.307 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
