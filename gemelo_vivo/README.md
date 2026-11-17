# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 09:17 (hora de Ciudad de México).

## Último pronóstico: 17/11 09:17 a 10:17

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
| 107-108 Tolsa-Balderas | 0 / 54 | 1.00 | 0.00 | 3-13 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 2-12 |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.01 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.99 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (27/30) a 107-108 (0/54)
2. Llevar **10 bicis** de 008 (17/17) a 555 (0/31)
3. Llevar **6 bicis** de 116 (12/17) a 270 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

24 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.134 | 0.043 |
| Sin resincronizar | 0.133 | 0.062 |
| Persistencia | 0.343 | 0.106 |
| Persistencia 0/1 | 0.343 | 0.106 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
