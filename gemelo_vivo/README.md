# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 12:09 (hora de Ciudad de México).

## Último pronóstico: 23/11 12:09 a 13:09

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.6 °C** · lluvia 0.2 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.87 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 20 | 0.81 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.81 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 1 / 27 | 0.76 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 3 / 23 | 0.72 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.72 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (24/30) a 555 (0/29)
2. Llevar **7 bicis** de 118 (15/18) a 041 (0/32)
3. Llevar **8 bicis** de 029 (16/34) a 086 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

462 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.254 | 0.088 |
| Persistencia | 0.292 | 0.063 |
| Persistencia 0/1 | 0.292 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
