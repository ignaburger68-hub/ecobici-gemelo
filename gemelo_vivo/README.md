# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 22:53 (hora de Ciudad de México).

## Último pronóstico: 20/11 22:52 a 23:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 3 km/h · día hábil

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
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.66 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.58 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.50 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 2 / 15 | 0.37 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 2 / 17 | 0.36 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 5 / 9 | 0.36 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 16 / 18 | 0.00 | 0.32 | 11-18 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (16/18) a 020 (0/22)
2. Llevar **11 bicis** de 450 (21/28) a 115 (0/26)
3. Llevar **7 bicis** de 029 (26/30) a 086 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

294 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.261 | 0.092 |
| Persistencia | 0.298 | 0.067 |
| Persistencia 0/1 | 0.298 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
