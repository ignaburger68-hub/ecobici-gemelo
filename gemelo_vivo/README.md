# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 19:19 (hora de Ciudad de México).

## Último pronóstico: 20/11 19:19 a 20:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 22 | 1.00 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 13 | 0.99 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.96 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 16 | 0.96 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 555 (30/33) a 003 (1/27)
2. Llevar **12 bicis** de 029 (32/33) a 086 (0/14)
3. Llevar **12 bicis** de 260 (18/20) a 010 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

279 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.267 | 0.093 |
| Persistencia | 0.304 | 0.066 |
| Persistencia 0/1 | 0.304 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
