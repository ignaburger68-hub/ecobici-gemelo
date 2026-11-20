# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 16:13 (hora de Ciudad de México).

## Último pronóstico: 20/11 16:13 a 17:13

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 9-15 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.97 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.97 | 0.00 | 0-7 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.94 | 18-23 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.94 | 16-22 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.87 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 25 | 0.86 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 11 | 0.74 | 0.03 | 0-7 |
| 256 Gómez Farías-Sadi Carnot | 3 / 22 | 0.58 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 116 (22/22) a 270 (1/25)
2. Llevar **13 bicis** de 114 (23/23) a 041 (1/29)
3. Llevar **9 bicis** de 113 (15/15) a 010 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

266 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.272 | 0.092 |
| Persistencia | 0.309 | 0.067 |
| Persistencia 0/1 | 0.309 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
