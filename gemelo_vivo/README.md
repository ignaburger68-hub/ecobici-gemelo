# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 21:41 (hora de Ciudad de México).

## Último pronóstico: 20/11 21:41 a 22:41

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
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.98 | 13-19 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.71 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.70 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 30 / 31 | 0.00 | 0.60 | 24-31 |
| 118 Liverpool-Dinamarca | 4 / 17 | 0.48 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 15 | 0.46 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 24 / 31 | 0.00 | 0.42 | 23-31 |
| 115 Roma-Dinamarca | 4 / 27 | 0.38 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 260 (19/19) a 086 (2/15)
2. Llevar **12 bicis** de 555 (24/31) a 112 (0/20)
3. Llevar **7 bicis** de 029 (30/31) a 012 (1/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

289 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.035 |
| Sin resincronizar | 0.263 | 0.092 |
| Persistencia | 0.301 | 0.067 |
| Persistencia 0/1 | 0.301 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
