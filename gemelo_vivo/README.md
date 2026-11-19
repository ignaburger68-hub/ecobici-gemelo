# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 06:52 (hora de Ciudad de México).

## Último pronóstico: 19/11 06:52 a 07:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.2 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 114 Lucerna-Abraham González | 0 / 18 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.98 | 0.00 | 0-8 |
| 048 Independencia - Azueta | 0 / 9 | 0.98 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.98 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 11 | 0.84 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.72 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.72 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 20 / 27 | 0.00 | 0.66 | 13-24 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 010 (20/27) a 256 (0/18)
2. Llevar **11 bicis** de 450 (22/25) a 555 (12/28)
3. Llevar **3 bicis** de 118 (3/14) a 086 (2/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

156 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.291 | 0.093 |
| Persistencia | 0.334 | 0.069 |
| Persistencia 0/1 | 0.334 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
