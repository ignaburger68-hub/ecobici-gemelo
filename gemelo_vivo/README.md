# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 22:46 (hora de Ciudad de México).

## Último pronóstico: 18/11 22:46 a 23:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.5 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.99 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 0 / 14 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 14 | 0.99 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 27 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 11 | 0.99 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.96 | 0.00 | 0-1 |
| 260 Av. Juárez-Balderas | 17 / 17 | 0.00 | 0.96 | 9-16 |
| 020 Reforma- Río Támesis | 1 / 13 | 0.91 | 0.00 | 0-1 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 450 (24/25) a 012 (1/14)
2. Llevar **12 bicis** de 112 (18/19) a 119 (0/27)
3. Llevar **7 bicis** de 260 (17/17) a 116 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

151 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.296 | 0.092 |
| Persistencia | 0.340 | 0.069 |
| Persistencia 0/1 | 0.340 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
