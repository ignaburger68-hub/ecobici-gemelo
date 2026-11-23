# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 13:20 (hora de Ciudad de México).

## Último pronóstico: 23/11 13:20 a 14:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.7 °C** · lluvia 0.1 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.89** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 12 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.94 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 19 | 0.94 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 29 | 0.93 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.89 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.70 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (23/30) a 041 (0/32)
2. Llevar **10 bicis** de 115 (19/24) a 010 (0/25)
3. Llevar **11 bicis** de 450 (14/30) a 555 (1/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

467 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.063 |
| Persistencia 0/1 | 0.291 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
