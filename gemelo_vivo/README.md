# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 08:35 (hora de Ciudad de México).

## Último pronóstico: 17/11 08:35 a 09:35

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 003 Reforma - Insurgentes | 0 / 31 | 1.00 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 26 | 1.00 | 0.00 | 0-1 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 0 / 20 | 1.00 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 15 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 9 | 1.00 | 0.01 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (28/30) a 270 (0/26)
2. Llevar **11 bicis** de 008 (13/17) a 259 (0/24)
3. Llevar **9 bicis** de 116 (12/18) a 255 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

21 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.100 | 0.051 |
| Sin resincronizar | 0.127 | 0.054 |
| Persistencia | 0.324 | 0.128 |
| Persistencia 0/1 | 0.324 | 0.128 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
