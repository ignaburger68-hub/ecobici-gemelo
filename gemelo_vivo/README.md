# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 18:46 (hora de Ciudad de México).

## Último pronóstico: 19/11 18:46 a 19:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.96 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 25 | 0.96 | 0.00 | 1-8 |
| 010 Reforma - Ramírez | 2 / 27 | 0.94 | 0.00 | 0-7 |
| 117 Londres-Nápoles | 1 / 26 | 0.92 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 2 / 13 | 0.89 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 1 / 32 | 0.88 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 555 (18/29) a 115 (2/25)
2. Llevar **10 bicis** de 260 (13/20) a 020 (0/21)
3. Llevar **13 bicis** de 029 (20/32) a 010 (2/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

206 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.300 | 0.097 |
| Persistencia | 0.336 | 0.069 |
| Persistencia 0/1 | 0.336 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
