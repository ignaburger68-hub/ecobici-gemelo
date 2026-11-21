# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 21:56 (hora de Ciudad de México).

## Último pronóstico: 20/11 21:56 a 22:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 012 Río Lerma - Villalongín | 0 / 13 | 1.00 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.98 | 11-18 |
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 0.97 | 26-31 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.96 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.77 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.62 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 2 / 21 | 0.51 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 3 / 28 | 0.49 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 3 / 15 | 0.21 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (19/19) a 086 (2/15)
2. Llevar **9 bicis** de 029 (31/31) a 012 (0/13)
3. Llevar **10 bicis** de 555 (22/31) a 115 (2/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

290 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.035 |
| Sin resincronizar | 0.262 | 0.092 |
| Persistencia | 0.300 | 0.067 |
| Persistencia 0/1 | 0.300 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
