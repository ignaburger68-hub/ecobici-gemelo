# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 13:17 (hora de Ciudad de México).

## Último pronóstico: 25/11 13:17 a 14:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

Sin datos de clima para esta hora: se toma como normal.

El clima multiplica los **retiros por 1.00** y las **devoluciones por 1.00** (1,00 = sin efecto).

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.97 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.95 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.94 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 1 / 30 | 0.86 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.83 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 3 / 26 | 0.75 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 116 (22/23) a 041 (0/31)
2. Llevar **12 bicis** de 115 (23/25) a 086 (0/17)
3. Llevar **16 bicis** de 031 (29/34) a 555 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

609 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
