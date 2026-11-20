# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 09:17 (hora de Ciudad de México).

## Último pronóstico: 20/11 09:17 a 10:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 31 / 31 | 0.00 | 1.00 | 23-31 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.92 | 12-15 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.89 | 6-11 |
| 010 Reforma - Ramírez | 26 / 27 | 0.00 | 0.87 | 22-27 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.72 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.69 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 2 / 31 | 0.47 | 0.00 | 1-8 |
| 086 Sullivan-Insurgentes | 3 / 17 | 0.46 | 0.00 | 0-8 |
| 008 Reforma - General Prim | 9 / 16 | 0.00 | 0.35 | 8-16 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (31/31) a 263 (1/29)
2. Llevar **10 bicis** de 113 (14/15) a 256 (1/23)
3. Llevar **14 bicis** de 010 (26/27) a 003 (2/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

237 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.285 | 0.092 |
| Persistencia | 0.323 | 0.063 |
| Persistencia 0/1 | 0.323 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
