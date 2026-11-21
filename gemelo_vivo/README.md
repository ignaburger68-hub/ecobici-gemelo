# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 22:10 (hora de Ciudad de México).

## Último pronóstico: 20/11 22:10 a 23:10

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
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.98 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.78 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.60 | 11-18 |
| 029 Reforma - Bucareli | 30 / 31 | 0.00 | 0.58 | 25-31 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.50 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.46 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 15 | 0.41 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (30/31) a 086 (0/15)
2. Llevar **7 bicis** de 260 (18/19) a 114 (0/21)
3. Llevar **10 bicis** de 555 (21/31) a 115 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

291 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.262 | 0.092 |
| Persistencia | 0.300 | 0.067 |
| Persistencia 0/1 | 0.300 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
