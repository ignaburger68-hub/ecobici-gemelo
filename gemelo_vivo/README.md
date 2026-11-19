# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 20:09 (hora de Ciudad de México).

## Último pronóstico: 18/11 20:09 a 21:09

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
| 115 Roma-Dinamarca | 0 / 21 | 1.00 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 13 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 7 | 0.97 | 0.04 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 9 | 0.97 | 0.03 | 0-4 |
| 026 Reforma - Versalles | 2 / 9 | 0.95 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 12 | 0.93 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 11 / 11 | 0.04 | 0.92 | 6-11 |
| 119 Turín-Abraham González | 1 / 27 | 0.92 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (17/18) a 115 (0/21)
2. Llevar **15 bicis** de 255 (21/30) a 117 (0/28)
3. Llevar **16 bicis** de 263 (21/29) a 031 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

140 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.304 | 0.086 |
| Persistencia | 0.345 | 0.067 |
| Persistencia 0/1 | 0.345 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
