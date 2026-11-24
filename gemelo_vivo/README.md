# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 12:49 (hora de Ciudad de México).

## Último pronóstico: 24/11 12:49 a 13:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.2 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.76** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 11-15 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.96 | 7-13 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.90 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.88 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.77 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.72 | 0.02 | 0-6 |
| 112 Av. Morelos-Abraham González | 2 / 19 | 0.71 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.67 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.65 | 0.00 | 1-8 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 24 | 0.63 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (15/15) a 041 (1/31)
2. Llevar **7 bicis** de 026 (13/13) a 270 (1/27)
3. Llevar **9 bicis** de 114 (17/22) a 260 (2/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

536 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.241 | 0.085 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
