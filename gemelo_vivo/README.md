# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 09:57 (hora de Ciudad de México).

## Último pronóstico: 25/11 09:57 a 10:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · lluvia 0.1 mm/h · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 17 | 1.00 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.96 | 0.00 | 0-7 |
| 098 Emilio Dondé-Av. Balderas | 0 / 13 | 0.95 | 0.00 | 1-7 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.76 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.71 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 11 / 12 | 0.00 | 0.71 | 8-12 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (29/32) a 086 (0/17)
2. Llevar **7 bicis** de 026 (11/12) a 041 (0/31)
3. Llevar **13 bicis** de 115 (23/25) a 555 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

595 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.081 |
| Persistencia | 0.267 | 0.060 |
| Persistencia 0/1 | 0.267 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
