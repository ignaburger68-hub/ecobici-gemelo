# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 13:45 (hora de Ciudad de México).

## Último pronóstico: 24/11 13:45 a 14:45

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
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.99 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.99 | 0.00 | 0-8 |
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.98 | 0.00 | 0-8 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.97 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.82 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.79 | 0.02 | 0-6 |
| 114 Lucerna-Abraham González | 21 / 22 | 0.00 | 0.78 | 15-22 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 114 (21/22) a 041 (0/32)
2. Llevar **9 bicis** de 113 (12/14) a 555 (0/30)
3. Llevar **12 bicis** de 031 (29/35) a 260 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

540 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.242 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
