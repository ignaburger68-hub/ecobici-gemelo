# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 08:20 (hora de Ciudad de México).

## Último pronóstico: 18/11 08:20 a 09:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 270 De la República-Ponciano Arr | 0 / 22 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 26 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 3 / 24 | 0.99 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.98 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.97 | 0.04 | 3-15 |
| 113 General Prim-Versalles | 8 / 9 | 0.01 | 0.97 | 7-9 |
| 119 Turín-Abraham González | 1 / 25 | 0.94 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 20 | 0.86 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 117 (14/30) a 270 (0/22)
2. Llevar **8 bicis** de 113 (8/9) a 555 (0/26)
3. Llevar **9 bicis** de 031 (10/30) a 259 (3/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

91 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.025 |
| Sin resincronizar | 0.316 | 0.089 |
| Persistencia | 0.355 | 0.044 |
| Persistencia 0/1 | 0.355 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
