# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 10:57 (hora de Ciudad de México).

## Último pronóstico: 19/11 10:57 a 11:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 555 Ribera de San Cosme - Insurg | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 14 / 14 | 0.00 | 0.98 | 10-14 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.98 | 8-13 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.96 | 10-17 |
| 116 Londres-Roma | 18 / 18 | 0.00 | 0.93 | 10-18 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (14/14) a 555 (0/28)
2. Llevar **14 bicis** de 117 (26/28) a 256 (1/20)
3. Llevar **8 bicis** de 113 (13/13) a 041 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

173 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.037 |
| Sin resincronizar | 0.275 | 0.091 |
| Persistencia | 0.330 | 0.070 |
| Persistencia 0/1 | 0.330 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
