# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 09:31 (hora de Ciudad de México).

## Último pronóstico: 18/11 09:31 a 10:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 31 / 31 | 0.00 | 1.00 | 15-29 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 10 / 10 | 0.00 | 0.99 | 8-10 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 7-11 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 0.98 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 0 / 27 | 0.98 | 0.00 | 1-9 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.98 | 0.00 | 4-17 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.97 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.97 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (31/31) a 119 (0/27)
2. Llevar **7 bicis** de 113 (10/10) a 107-108 (0/55)
3. Llevar **11 bicis** de 115 (21/22) a 256 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

96 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.025 |
| Sin resincronizar | 0.315 | 0.086 |
| Persistencia | 0.360 | 0.045 |
| Persistencia 0/1 | 0.360 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
