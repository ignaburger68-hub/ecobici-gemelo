# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 09:19 (hora de Ciudad de México).

## Último pronóstico: 23/11 09:19 a 10:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.0 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 107-108 Tolsa-Balderas | 0 / 56 | 1.00 | 0.00 | 2-10 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.98 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.95 | 17-28 |
| 119 Turín-Abraham González | 2 / 27 | 0.94 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 117 (29/30) a 010 (1/27)
2. Llevar **12 bicis** de 115 (18/24) a 107-108 (0/56)
3. Llevar **8 bicis** de 555 (16/31) a 086 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

450 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.257 | 0.089 |
| Persistencia | 0.295 | 0.064 |
| Persistencia 0/1 | 0.295 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
