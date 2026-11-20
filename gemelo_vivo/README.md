# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 19:57 (hora de Ciudad de México).

## Último pronóstico: 19/11 19:57 a 20:57

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
| 008 Reforma - General Prim | 0 / 16 | 0.98 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.93 | 16-20 |
| 114 Lucerna-Abraham González | 0 / 22 | 0.93 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.92 | 8-15 |
| 116 Londres-Roma | 1 / 20 | 0.73 | 0.00 | 1-10 |
| 256 Gómez Farías-Sadi Carnot | 19 / 23 | 0.00 | 0.67 | 15-23 |
| 113 General Prim-Versalles | 10 / 13 | 0.01 | 0.61 | 5-13 |
| 118 Liverpool-Dinamarca | 2 / 19 | 0.59 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 25 / 32 | 0.00 | 0.52 | 21-32 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (19/20) a 008 (0/16)
2. Llevar **8 bicis** de 026 (13/15) a 116 (1/20)
3. Llevar **11 bicis** de 256 (19/23) a 003 (4/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

211 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
