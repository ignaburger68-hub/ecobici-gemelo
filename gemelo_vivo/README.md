# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 13:17 (hora de Ciudad de México).

## Último pronóstico: 24/11 13:17 a 14:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.75** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 13 / 13 | 0.01 | 0.97 | 7-13 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.96 | 9-18 |
| 119 Turín-Abraham González | 0 / 26 | 0.96 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.95 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.81 | 0.01 | 0-6 |
| 113 General Prim-Versalles | 12 / 14 | 0.00 | 0.78 | 10-14 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.75 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.73 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.70 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (12/14) a 041 (0/32)
2. Llevar **9 bicis** de 118 (19/19) a 260 (1/20)
3. Llevar **7 bicis** de 026 (13/13) a 119 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

538 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.241 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
