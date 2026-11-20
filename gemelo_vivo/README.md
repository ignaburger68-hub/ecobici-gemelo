# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 19:43 (hora de Ciudad de México).

## Último pronóstico: 19/11 19:43 a 20:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 16-21 |
| 008 Reforma - General Prim | 0 / 15 | 0.96 | 0.00 | 0-3 |
| 116 Londres-Roma | 1 / 20 | 0.88 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 12 / 14 | 0.01 | 0.86 | 5-13 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.82 | 0.01 | 0-10 |
| 256 Gómez Farías-Sadi Carnot | 21 / 23 | 0.00 | 0.79 | 16-23 |
| 555 Ribera de San Cosme - Insurg | 31 / 35 | 0.00 | 0.65 | 24-35 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.54 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 5 / 30 | 0.38 | 0.00 | 0-10 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (21/21) a 116 (1/20)
2. Llevar **9 bicis** de 256 (21/23) a 086 (1/17)
3. Llevar **10 bicis** de 555 (31/35) a 008 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

210 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.298 | 0.097 |
| Persistencia | 0.336 | 0.068 |
| Persistencia 0/1 | 0.336 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
