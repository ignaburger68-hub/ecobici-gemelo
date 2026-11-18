# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 17:07 (hora de Ciudad de México).

## Último pronóstico: 18/11 17:07 a 18:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 13 / 13 | 0.00 | 0.97 | 7-13 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.97 | 0.00 | 1-7 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.96 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 25 | 0.96 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.93 | 0.01 | 0-5 |
| 031 Hamburgo - Insurgentes | 29 / 29 | 0.00 | 0.93 | 15-28 |
| 086 Sullivan-Insurgentes | 10 / 11 | 0.05 | 0.85 | 5-11 |
| 119 Turín-Abraham González | 1 / 27 | 0.84 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 2 / 23 | 0.76 | 0.00 | 1-10 |
| 026 Reforma - Versalles | 3 / 10 | 0.74 | 0.02 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 012 (13/13) a 010 (1/25)
2. Llevar **6 bicis** de 086 (10/11) a 020 (1/10)
3. Llevar **11 bicis** de 031 (29/29) a 119 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

128 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.033 |
| Sin resincronizar | 0.305 | 0.085 |
| Persistencia | 0.342 | 0.064 |
| Persistencia 0/1 | 0.342 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
