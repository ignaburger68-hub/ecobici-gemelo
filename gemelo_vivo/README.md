# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 09:32 (hora de Ciudad de México).

## Último pronóstico: 17/11 09:32 a 10:32

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**15.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 54 | 1.00 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-8 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 117 (29/30) a 119 (0/25)
2. Llevar **10 bicis** de 008 (16/17) a 085 (0/14)
3. Llevar **6 bicis** de 117 (29/30) a 555 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

25 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.136 | 0.045 |
| Sin resincronizar | 0.141 | 0.070 |
| Persistencia | 0.344 | 0.103 |
| Persistencia 0/1 | 0.344 | 0.103 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
