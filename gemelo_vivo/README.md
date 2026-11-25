# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 12:18 (hora de Ciudad de México).

## Último pronóstico: 25/11 12:18 a 13:18

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
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 0.86 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.81 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.79 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 1 / 27 | 0.72 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.72 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 3 / 21 | 0.71 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.70 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (26/28) a 555 (2/30)
2. Llevar **10 bicis** de 115 (23/25) a 041 (0/30)
3. Llevar **13 bicis** de 031 (30/34) a 270 (2/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

605 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.264 | 0.060 |
| Persistencia 0/1 | 0.264 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
