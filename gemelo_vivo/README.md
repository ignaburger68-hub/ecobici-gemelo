# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 10:57 (hora de Ciudad de México).

## Último pronóstico: 20/11 10:57 a 11:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 086 Sullivan-Insurgentes | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 21 / 21 | 0.00 | 0.97 | 14-21 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.95 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 32 | 0.95 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.95 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 28 / 29 | 0.00 | 0.94 | 24-29 |
| 048 Independencia - Azueta | 10 / 10 | 0.01 | 0.93 | 5-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.88 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 24 / 25 | 0.00 | 0.85 | 19-25 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (28/29) a 555 (2/32)
2. Llevar **15 bicis** de 115 (24/25) a 256 (1/22)
3. Llevar **12 bicis** de 114 (21/21) a 107-108 (1/56)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

244 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.280 | 0.091 |
| Persistencia | 0.319 | 0.064 |
| Persistencia 0/1 | 0.319 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
