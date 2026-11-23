# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 15:15 (hora de Ciudad de México).

## Último pronóstico: 23/11 15:15 a 16:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.87** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.96 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 26 | 0.95 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.87 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 19 | 0.86 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 3 / 11 | 0.85 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.85 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 2 / 18 | 0.79 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 3 / 19 | 0.76 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (26/29) a 010 (1/26)
2. Llevar **13 bicis** de 031 (24/35) a 041 (0/32)
3. Llevar **10 bicis** de 029 (19/34) a 260 (3/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

475 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.061 |
| Persistencia 0/1 | 0.291 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
