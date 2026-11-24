# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 14:00 (hora de Ciudad de México).

## Último pronóstico: 24/11 14:00 a 15:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · lluvia 0.4 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.75** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.01 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.99 | 0.00 | 0-7 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 14 / 14 | 0.01 | 0.98 | 6-14 |
| 114 Lucerna-Abraham González | 22 / 22 | 0.00 | 0.95 | 13-21 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.94 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 16 | 0.88 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.81 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (14/14) a 270 (0/27)
2. Llevar **11 bicis** de 116 (20/23) a 041 (0/32)
3. Llevar **12 bicis** de 114 (22/22) a 256 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

541 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.241 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
