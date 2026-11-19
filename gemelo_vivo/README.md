# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 09:57 (hora de Ciudad de México).

## Último pronóstico: 19/11 09:57 a 10:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.99 | 9-13 |
| 114 Lucerna-Abraham González | 18 / 18 | 0.00 | 0.99 | 12-18 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.93 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 13 / 14 | 0.00 | 0.89 | 10-14 |
| 118 Liverpool-Dinamarca | 10 / 14 | 0.00 | 0.76 | 10-14 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.70 | 0.00 | 0-8 |
| 041 Reforma - Av. de la Repúblic | 2 / 25 | 0.69 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 113 (13/13) a 086 (0/16)
2. Llevar **10 bicis** de 114 (18/18) a 020 (0/19)
3. Llevar **8 bicis** de 118 (10/14) a 041 (2/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

169 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.036 |
| Sin resincronizar | 0.278 | 0.090 |
| Persistencia | 0.332 | 0.069 |
| Persistencia 0/1 | 0.332 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
