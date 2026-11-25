# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 09:43 (hora de Ciudad de México).

## Último pronóstico: 25/11 09:43 a 10:43

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
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.98 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.93 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 12 | 0.92 | 0.01 | 1-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.86 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.85 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.79 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 029 (25/32) a 555 (0/30)
2. Llevar **12 bicis** de 115 (22/24) a 041 (0/31)
3. Llevar **12 bicis** de 031 (27/34) a 086 (1/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

594 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
