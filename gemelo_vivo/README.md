# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 21:27 (hora de Ciudad de México).

## Último pronóstico: 20/11 21:27 a 22:27

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
| 012 Río Lerma - Villalongín | 0 / 13 | 1.00 | 0.00 | 0-2 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.97 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.78 | 14-19 |
| 118 Liverpool-Dinamarca | 3 / 17 | 0.63 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.57 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 2 / 15 | 0.56 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 12 / 13 | 0.01 | 0.47 | 6-13 |
| 029 Reforma - Bucareli | 29 / 31 | 0.00 | 0.45 | 23-30 |
| 048 Independencia - Azueta | 7 / 10 | 0.00 | 0.43 | 5-10 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 260 (18/19) a 012 (0/13)
2. Llevar **11 bicis** de 555 (25/32) a 112 (0/20)
3. Llevar **9 bicis** de 029 (29/31) a 118 (3/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

288 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.035 |
| Sin resincronizar | 0.263 | 0.093 |
| Persistencia | 0.302 | 0.067 |
| Persistencia 0/1 | 0.302 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
