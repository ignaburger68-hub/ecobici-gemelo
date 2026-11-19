# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 12:22 (hora de Ciudad de México).

## Último pronóstico: 19/11 12:22 a 13:22

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
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 1.00 | 0.00 | 0-1 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.98 | 10-17 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 0.97 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 114 (17/17) a 255 (0/31)
2. Llevar **16 bicis** de 117 (26/27) a 041 (0/24)
3. Llevar **10 bicis** de 116 (17/17) a 555 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

179 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.037 |
| Sin resincronizar | 0.273 | 0.093 |
| Persistencia | 0.329 | 0.071 |
| Persistencia 0/1 | 0.329 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
