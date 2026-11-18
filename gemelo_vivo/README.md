# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 08:04 (hora de Ciudad de México).

## Último pronóstico: 18/11 08:04 a 09:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 0 / 17 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 3 / 24 | 0.99 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 2 / 27 | 0.99 | 0.00 | 0-1 |
| 270 De la República-Ponciano Arr | 4 / 22 | 0.97 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 1 / 26 | 0.96 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 1 / 7 | 0.95 | 0.11 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 2 / 28 | 0.94 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **6 bicis** de 113 (6/10) a 555 (2/27)
2. Llevar **7 bicis** de 117 (7/30) a 256 (0/19)
3. Llevar **7 bicis** de 031 (7/31) a 259 (3/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

90 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.025 |
| Sin resincronizar | 0.315 | 0.090 |
| Persistencia | 0.352 | 0.044 |
| Persistencia 0/1 | 0.352 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
