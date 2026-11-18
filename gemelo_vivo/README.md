# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 10:14 (hora de Ciudad de México).

## Último pronóstico: 18/11 10:13 a 11:13

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 8-11 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 0 / 10 | 0.98 | 0.01 | 0-5 |
| 114 Lucerna-Abraham González | 17 / 18 | 0.00 | 0.96 | 13-18 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.96 | 28-30 |
| 119 Turín-Abraham González | 0 / 27 | 0.92 | 0.00 | 1-10 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.92 | 29-33 |
| 115 Roma-Dinamarca | 20 / 21 | 0.00 | 0.89 | 18-21 |
| 113 General Prim-Versalles | 0 / 11 | 0.80 | 0.24 | 2-11 |
| 118 Liverpool-Dinamarca | 9 / 13 | 0.00 | 0.78 | 9-13 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (29/30) a 098 (1/30)
2. Llevar **7 bicis** de 026 (11/11) a 048 (0/10)
3. Llevar **12 bicis** de 114 (17/18) a 270 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

99 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.026 |
| Sin resincronizar | 0.313 | 0.085 |
| Persistencia | 0.358 | 0.048 |
| Persistencia 0/1 | 0.358 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
