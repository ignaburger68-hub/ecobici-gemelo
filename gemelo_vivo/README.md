# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 20:24 (hora de Ciudad de México).

## Último pronóstico: 18/11 20:23 a 21:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 13 | 1.00 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 21 | 1.00 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.97 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 1 / 30 | 0.96 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 2 / 9 | 0.95 | 0.01 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.94 | 0.09 | 0-3 |
| 048 Independencia - Azueta | 1 / 8 | 0.83 | 0.03 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 24 | 0.75 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 2 / 27 | 0.75 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 450 (20/25) a 117 (0/28)
2. Llevar **9 bicis** de 260 (16/18) a 031 (1/30)
3. Llevar **10 bicis** de 112 (17/19) a 115 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

141 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.034 |
| Sin resincronizar | 0.304 | 0.086 |
| Persistencia | 0.344 | 0.067 |
| Persistencia 0/1 | 0.344 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
