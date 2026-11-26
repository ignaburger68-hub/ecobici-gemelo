# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 11:35 (hora de Ciudad de México).

## Último pronóstico: 26/11 11:34 a 12:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · lluvia 0.1 mm/h · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.88 | 1.00 | 1-1 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 1.00 | 24-27 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.90 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 11 | 0.84 | 0.35 | 4-11 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.77 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.71 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.69 | 16-21 |
| 256 Gómez Farías-Sadi Carnot | 2 / 23 | 0.56 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (27/27) a 041 (1/32)
2. Llevar **8 bicis** de 260 (19/21) a 008 (0/12)
3. Llevar **11 bicis** de 114 (19/22) a 259 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

673 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
