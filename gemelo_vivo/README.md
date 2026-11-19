# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 12:08 (hora de Ciudad de México).

## Último pronóstico: 19/11 12:08 a 13:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.9 °C** · sin lluvia · viento 4 km/h · día hábil

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
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.99 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 20 | 0.98 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.98 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (26/27) a 555 (1/30)
2. Llevar **11 bicis** de 114 (17/17) a 086 (1/16)
3. Llevar **9 bicis** de 116 (16/17) a 010 (2/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

178 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.037 |
| Sin resincronizar | 0.273 | 0.092 |
| Persistencia | 0.329 | 0.070 |
| Persistencia 0/1 | 0.329 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
