# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 21:13 (hora de Ciudad de México).

## Último pronóstico: 20/11 21:13 a 22:13

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 0.97 | 25-31 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.96 | 14-19 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.84 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 3 / 22 | 0.66 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.64 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.61 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 2 / 17 | 0.57 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 15 | 0.55 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 4 / 15 | 0.42 | 0.01 | 0-9 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (31/31) a 012 (1/13)
2. Llevar **10 bicis** de 260 (19/19) a 020 (3/22)
3. Llevar **13 bicis** de 555 (27/33) a 003 (3/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

287 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.035 |
| Sin resincronizar | 0.264 | 0.093 |
| Persistencia | 0.303 | 0.067 |
| Persistencia 0/1 | 0.303 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
