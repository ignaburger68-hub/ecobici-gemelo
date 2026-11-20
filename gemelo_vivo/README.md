# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 08:20 (hora de Ciudad de México).

## Último pronóstico: 20/11 08:20 a 09:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 29 | 0.94 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 10 | 0.92 | 0.05 | 0-6 |
| 086 Sullivan-Insurgentes | 4 / 15 | 0.84 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 7 / 28 | 0.84 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 11 | 0.81 | 0.01 | 0-5 |
| 113 General Prim-Versalles | 4 / 14 | 0.01 | 0.79 | 11-14 |
| 260 Av. Juárez-Balderas | 3 / 20 | 0.77 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 116 (16/21) a 555 (3/29)
2. Llevar **12 bicis** de 117 (13/29) a 256 (1/23)
3. Llevar **4 bicis** de 113 (4/14) a 263 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

233 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.286 | 0.093 |
| Persistencia | 0.324 | 0.063 |
| Persistencia 0/1 | 0.324 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
