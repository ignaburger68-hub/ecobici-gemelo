# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 08:18 (hora de Ciudad de México).

## Último pronóstico: 19/11 08:17 a 09:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 1.00 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 3 / 25 | 1.00 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 1 / 18 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 9 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 10 | 1.00 | 0.00 | 0-2 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 3 / 31 | 0.94 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (15/29) a 555 (0/25)
2. Llevar **12 bicis** de 115 (13/24) a 270 (3/25)
3. Llevar **9 bicis** de 116 (9/23) a 259 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

162 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.283 | 0.090 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
