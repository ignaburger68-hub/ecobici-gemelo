# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 10:28 (hora de Ciudad de México).

## Último pronóstico: 20/11 10:28 a 11:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 10-15 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-2 |
| 107-108 Tolsa-Balderas | 2 / 56 | 0.96 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 29 / 29 | 0.00 | 0.96 | 22-29 |
| 048 Independencia - Azueta | 10 / 10 | 0.15 | 0.91 | 1-9 |
| 115 Roma-Dinamarca | 24 / 25 | 0.00 | 0.90 | 20-25 |
| 114 Lucerna-Abraham González | 21 / 21 | 0.00 | 0.89 | 10-20 |
| 029 Reforma - Bucareli | 2 / 35 | 0.80 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (29/29) a 555 (0/31)
2. Llevar **17 bicis** de 115 (24/25) a 107-108 (2/56)
3. Llevar **11 bicis** de 113 (15/15) a 256 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

242 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.034 |
| Sin resincronizar | 0.281 | 0.091 |
| Persistencia | 0.320 | 0.063 |
| Persistencia 0/1 | 0.320 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
