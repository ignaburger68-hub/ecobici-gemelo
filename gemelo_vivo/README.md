# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 09:14 (hora de Ciudad de México).

## Último pronóstico: 19/11 09:14 a 10:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.5 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 113 General Prim-Versalles | 14 / 14 | 0.00 | 1.00 | 9-14 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.99 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 1-7 |
| 048 Independencia - Azueta | 0 / 10 | 0.95 | 0.03 | 0-7 |
| 116 Londres-Roma | 20 / 21 | 0.00 | 0.95 | 14-21 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.90 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.90 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 113 (14/14) a 270 (1/27)
2. Llevar **13 bicis** de 116 (20/21) a 255 (2/33)
3. Llevar **9 bicis** de 115 (23/26) a 086 (2/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

166 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.281 | 0.089 |
| Persistencia | 0.333 | 0.067 |
| Persistencia 0/1 | 0.333 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
