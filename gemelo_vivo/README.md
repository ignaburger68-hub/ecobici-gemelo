# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 10:14 (hora de Ciudad de México).

## Último pronóstico: 20/11 10:14 a 11:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 12-15 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.97 | 0.00 | 0-7 |
| 117 Londres-Nápoles | 27 / 29 | 0.00 | 0.89 | 26-29 |
| 114 Lucerna-Abraham González | 19 / 21 | 0.00 | 0.83 | 14-21 |
| 115 Roma-Dinamarca | 24 / 25 | 0.00 | 0.79 | 20-25 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.77 | 0.00 | 0-6 |
| 107-108 Tolsa-Balderas | 0 / 56 | 0.77 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 113 (15/15) a 256 (0/23)
2. Llevar **17 bicis** de 117 (27/29) a 041 (0/30)
3. Llevar **9 bicis** de 114 (19/21) a 086 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

241 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.034 |
| Sin resincronizar | 0.282 | 0.091 |
| Persistencia | 0.321 | 0.063 |
| Persistencia 0/1 | 0.321 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
