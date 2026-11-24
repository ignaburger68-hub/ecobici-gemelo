# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 12:06 (hora de Ciudad de México).

## Último pronóstico: 24/11 12:06 a 13:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · lluvia 0.5 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.84 | 10-15 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.80 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.78 | 0.01 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.70 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 24 | 0.70 | 0.00 | 0-5 |
| 116 Londres-Roma | 20 / 23 | 0.00 | 0.62 | 17-23 |
| 026 Reforma - Versalles | 12 / 13 | 0.01 | 0.59 | 6-13 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (14/15) a 041 (0/32)
2. Llevar **11 bicis** de 116 (20/23) a 263 (0/28)
3. Llevar **11 bicis** de 031 (31/34) a 112 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

533 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.242 | 0.085 |
| Persistencia | 0.275 | 0.061 |
| Persistencia 0/1 | 0.275 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
