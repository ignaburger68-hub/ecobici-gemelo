# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 18:04 (hora de Ciudad de México).

## Último pronóstico: 18/11 18:04 a 19:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 10 | 1.00 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 11 | 1.00 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 2 / 28 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.98 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 3 / 21 | 0.98 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 10 / 29 | 0.94 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 10 | 0.93 | 0.01 | 0-5 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.93 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 6 / 9 | 0.80 | 0.23 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 107-108 (16/51) a 117 (2/28)
2. Llevar **10 bicis** de 555 (14/27) a 031 (10/29)
3. Llevar **8 bicis** de 116 (14/17) a 115 (3/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

132 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.309 | 0.086 |
| Persistencia | 0.343 | 0.066 |
| Persistencia 0/1 | 0.343 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
