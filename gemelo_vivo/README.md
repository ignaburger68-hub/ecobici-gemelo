# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 09:46 (hora de Ciudad de México).

## Último pronóstico: 20/11 09:46 a 10:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

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
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 11 / 11 | 0.03 | 0.99 | 3-11 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.69 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.66 | 22-30 |
| 010 Reforma - Ramírez | 1 / 23 | 0.63 | 0.00 | 1-11 |
| 086 Sullivan-Insurgentes | 3 / 17 | 0.55 | 0.00 | 0-6 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.47 | 0.00 | 1-14 |
| 263 Sadi Carnot - Gómez Farias | 2 / 29 | 0.45 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 113 (15/15) a 041 (0/30)
2. Llevar **12 bicis** de 117 (29/30) a 256 (1/23)
3. Llevar **5 bicis** de 048 (11/11) a 086 (3/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

239 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.284 | 0.092 |
| Persistencia | 0.322 | 0.063 |
| Persistencia 0/1 | 0.322 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
