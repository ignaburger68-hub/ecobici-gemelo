# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 18:37 (hora de Ciudad de México).

## Último pronóstico: 20/11 18:36 a 19:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 116 Londres-Roma | 22 / 22 | 0.01 | 0.98 | 8-20 |
| 008 Reforma - General Prim | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.98 | 16-20 |
| 029 Reforma - Bucareli | 30 / 32 | 0.00 | 0.98 | 25-32 |
| 048 Independencia - Azueta | 8 / 9 | 0.05 | 0.93 | 3-9 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.92 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.86 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 24 | 0.82 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 11 | 0.70 | 0.03 | 0-7 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 029 (30/32) a 020 (1/21)
2. Llevar **15 bicis** de 260 (19/20) a 115 (2/24)
3. Llevar **9 bicis** de 116 (22/22) a 008 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

276 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.268 | 0.094 |
| Persistencia | 0.305 | 0.067 |
| Persistencia 0/1 | 0.305 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
