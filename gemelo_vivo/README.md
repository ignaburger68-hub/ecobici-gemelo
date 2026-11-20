# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 19:15 (hora de Ciudad de México).

## Último pronóstico: 19/11 19:14 a 20:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 15 | 1.00 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 0 / 14 | 1.00 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 0 / 26 | 1.00 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.99 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.97 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 19 | 0.94 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.93 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 3 / 13 | 0.89 | 0.03 | 2-10 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.87 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (19/21) a 003 (0/29)
2. Llevar **10 bicis** de 555 (18/29) a 113 (0/14)
3. Llevar **11 bicis** de 255 (14/29) a 008 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

208 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.299 | 0.098 |
| Persistencia | 0.337 | 0.069 |
| Persistencia 0/1 | 0.337 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
