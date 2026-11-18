# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 08:34 (hora de Ciudad de México).

## Último pronóstico: 18/11 08:34 a 09:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 259 Tómas Alva Edison-Ponciano A | 0 / 22 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 28 | 1.00 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 3 / 22 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 2 / 9 | 0.97 | 0.01 | 0-2 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.97 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 1 / 26 | 0.96 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.94 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 2 / 24 | 0.94 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (19/31) a 270 (3/22)
2. Llevar **12 bicis** de 031 (13/30) a 555 (3/28)
3. Llevar **6 bicis** de 113 (6/9) a 259 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

92 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.025 |
| Sin resincronizar | 0.316 | 0.089 |
| Persistencia | 0.358 | 0.043 |
| Persistencia 0/1 | 0.358 | 0.043 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
