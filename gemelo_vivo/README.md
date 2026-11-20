# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 16:27 (hora de Ciudad de México).

## Último pronóstico: 20/11 16:27 a 17:27

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.98 | 17-22 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.97 | 17-23 |
| 010 Reforma - Ramírez | 2 / 25 | 0.87 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 11 | 0.85 | 0.01 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 29 | 0.81 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.78 | 0.01 | 0-6 |
| 003 Reforma - Insurgentes | 2 / 29 | 0.74 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 2 / 22 | 0.73 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 1 / 16 | 0.70 | 0.03 | 2-12 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 116 (22/22) a 010 (2/25)
2. Llevar **15 bicis** de 114 (23/23) a 041 (2/29)
3. Llevar **15 bicis** de 029 (27/33) a 003 (2/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

267 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.034 |
| Sin resincronizar | 0.271 | 0.092 |
| Persistencia | 0.309 | 0.067 |
| Persistencia 0/1 | 0.309 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
