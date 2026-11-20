# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 09:32 (hora de Ciudad de México).

## Último pronóstico: 20/11 09:31 a 10:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 31 / 31 | 0.00 | 1.00 | 24-31 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 13-15 |
| 048 Independencia - Azueta | 10 / 11 | 0.01 | 0.82 | 5-11 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.68 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 2 / 30 | 0.56 | 0.00 | 1-7 |
| 263 Sadi Carnot - Gómez Farias | 2 / 29 | 0.47 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 13 / 22 | 0.00 | 0.46 | 13-22 |
| 260 Av. Juárez-Balderas | 2 / 21 | 0.45 | 0.00 | 1-8 |
| 256 Gómez Farías-Sadi Carnot | 2 / 23 | 0.42 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (31/31) a 041 (2/30)
2. Llevar **10 bicis** de 113 (15/15) a 086 (1/17)
3. Llevar **9 bicis** de 114 (13/22) a 256 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

238 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
