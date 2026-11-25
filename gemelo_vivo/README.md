# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 12:04 (hora de Ciudad de México).

## Último pronóstico: 25/11 12:04 a 13:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 17 / 17 | 0.00 | 0.97 | 9-16 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.88 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 30 | 0.85 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.77 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 3 / 22 | 0.75 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.74 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.73 | 0.00 | 0-6 |
| 450 Ramos Arizpe- Av México Teno | 1 / 27 | 0.72 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 117 (25/28) a 555 (3/30)
2. Llevar **13 bicis** de 031 (33/35) a 270 (0/26)
3. Llevar **8 bicis** de 118 (17/17) a 256 (3/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

604 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.265 | 0.060 |
| Persistencia 0/1 | 0.265 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
