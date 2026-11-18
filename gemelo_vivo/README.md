# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 18:22 (hora de Ciudad de México).

## Último pronóstico: 17/11 18:22 a 19:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.2 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.88** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.11 | 0-4 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 26 | 1.00 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 1 / 23 | 1.00 | 0.00 | 0-8 |
| 118 Liverpool-Dinamarca | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 555 (25/28) a 031 (0/26)
2. Llevar **11 bicis** de 260 (12/18) a 117 (0/29)
3. Llevar **10 bicis** de 107-108 (14/49) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

62 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.149 | 0.027 |
| Sin resincronizar | 0.292 | 0.089 |
| Persistencia | 0.357 | 0.044 |
| Persistencia 0/1 | 0.357 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
