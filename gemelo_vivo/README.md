# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 11:11 (hora de Ciudad de México).

## Último pronóstico: 20/11 11:11 a 12:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 20 / 20 | 0.00 | 0.96 | 14-20 |
| 117 Londres-Nápoles | 29 / 29 | 0.00 | 0.95 | 24-29 |
| 555 Ribera de San Cosme - Insurg | 1 / 32 | 0.94 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 2 / 23 | 0.94 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 1 / 35 | 0.89 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.81 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.80 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.79 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (29/29) a 555 (1/32)
2. Llevar **11 bicis** de 114 (20/20) a 256 (2/23)
3. Llevar **9 bicis** de 113 (14/15) a 029 (1/35)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

245 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.279 | 0.091 |
| Persistencia | 0.318 | 0.064 |
| Persistencia 0/1 | 0.318 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
