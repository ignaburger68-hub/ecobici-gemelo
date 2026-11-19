# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 15:40 (hora de Ciudad de México).

## Último pronóstico: 19/11 15:40 a 16:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.0 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 30 | 0.99 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 19 | 0.96 | 0.00 | 1-7 |
| 270 De la República-Ponciano Arr | 1 / 23 | 0.96 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 21 | 0.94 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (10/13) a 010 (0/26)
2. Llevar **7 bicis** de 107-108 (11/57) a 255 (0/31)
3. Llevar **5 bicis** de 117 (15/25) a 029 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

193 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.037 |
| Sin resincronizar | 0.290 | 0.094 |
| Persistencia | 0.333 | 0.070 |
| Persistencia 0/1 | 0.333 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
