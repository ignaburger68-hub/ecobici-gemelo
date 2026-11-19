# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 21:06 (hora de Ciudad de México).

## Último pronóstico: 18/11 21:06 a 22:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 10 | 1.00 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 0 / 28 | 0.99 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 21 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.98 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 9 | 0.98 | 0.07 | 0-6 |
| 008 Reforma - General Prim | 0 / 13 | 0.95 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 23 | 0.83 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 17 / 18 | 0.00 | 0.63 | 11-18 |
| 116 Londres-Roma | 2 / 17 | 0.63 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 450 (21/24) a 031 (0/29)
2. Llevar **8 bicis** de 260 (17/18) a 020 (0/10)
3. Llevar **10 bicis** de 112 (17/19) a 115 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

144 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.034 |
| Sin resincronizar | 0.302 | 0.088 |
| Persistencia | 0.343 | 0.068 |
| Persistencia 0/1 | 0.343 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
