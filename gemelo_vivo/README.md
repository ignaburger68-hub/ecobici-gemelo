# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 18:22 (hora de Ciudad de México).

## Último pronóstico: 20/11 18:22 a 19:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.2 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 17-20 |
| 048 Independencia - Azueta | 9 / 9 | 0.01 | 0.99 | 4-9 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 13-21 |
| 008 Reforma - General Prim | 0 / 15 | 0.98 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 27 / 31 | 0.00 | 0.90 | 27-31 |
| 115 Roma-Dinamarca | 1 / 25 | 0.86 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 11 | 0.79 | 0.05 | 0-7 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.75 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.69 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 260 (20/20) a 115 (1/25)
2. Llevar **11 bicis** de 029 (27/31) a 008 (0/15)
3. Llevar **12 bicis** de 116 (22/22) a 020 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

275 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.269 | 0.094 |
| Persistencia | 0.306 | 0.067 |
| Persistencia 0/1 | 0.306 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
