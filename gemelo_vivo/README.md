# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 18:32 (hora de Ciudad de México).

## Último pronóstico: 18/11 18:32 a 19:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.2 °C** · lluvia 0.2 mm/h · viento 12 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 1 / 29 | 0.99 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.99 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 21 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.98 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.95 | 0.00 | 0-10 |
| 012 Río Lerma - Villalongín | 2 / 11 | 0.94 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 11 | 0.93 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 555 (25/27) a 031 (1/29)
2. Llevar **12 bicis** de 107-108 (18/51) a 115 (1/21)
3. Llevar **10 bicis** de 029 (13/27) a 117 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

134 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.308 | 0.086 |
| Persistencia | 0.344 | 0.066 |
| Persistencia 0/1 | 0.344 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
