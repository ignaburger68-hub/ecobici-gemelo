# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 20:45 (hora de Ciudad de México).

## Último pronóstico: 20/11 20:44 a 21:44

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 0 / 17 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.97 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 31 / 32 | 0.00 | 0.94 | 28-32 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.89 | 14-19 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.83 | 0.01 | 0-7 |
| 031 Hamburgo - Insurgentes | 31 / 33 | 0.00 | 0.73 | 28-33 |
| 113 General Prim-Versalles | 1 / 15 | 0.67 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 10 / 14 | 0.01 | 0.35 | 6-13 |
| 112 Av. Morelos-Abraham González | 3 / 21 | 0.28 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (31/32) a 086 (1/15)
2. Llevar **10 bicis** de 260 (18/19) a 118 (0/17)
3. Llevar **8 bicis** de 031 (31/33) a 012 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

285 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.265 | 0.093 |
| Persistencia | 0.304 | 0.067 |
| Persistencia 0/1 | 0.304 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
