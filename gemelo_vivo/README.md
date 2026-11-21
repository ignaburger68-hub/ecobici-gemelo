# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 18:51 (hora de Ciudad de México).

## Último pronóstico: 20/11 18:51 a 19:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 8 km/h · día hábil

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
| 048 Independencia - Azueta | 9 / 9 | 0.08 | 0.96 | 3-9 |
| 116 Londres-Roma | 22 / 22 | 0.04 | 0.95 | 5-19 |
| 008 Reforma - General Prim | 1 / 16 | 0.91 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.88 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 28 / 30 | 0.00 | 0.88 | 23-30 |
| 026 Reforma - Versalles | 1 / 12 | 0.88 | 0.01 | 0-6 |
| 020 Reforma- Río Támesis | 2 / 20 | 0.82 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 3 / 26 | 0.79 | 0.00 | 0-8 |
| 113 General Prim-Versalles | 4 / 15 | 0.58 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 029 (28/30) a 115 (3/26)
2. Llevar **10 bicis** de 450 (18/28) a 008 (1/16)
3. Llevar **5 bicis** de 048 (9/9) a 012 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

277 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.268 | 0.093 |
| Persistencia | 0.305 | 0.067 |
| Persistencia 0/1 | 0.305 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
