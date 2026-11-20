# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 15:30 (hora de Ciudad de México).

## Último pronóstico: 20/11 15:30 a 16:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.97 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.94 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.93 | 25-33 |
| 116 Londres-Roma | 22 / 22 | 0.01 | 0.89 | 10-20 |
| 115 Roma-Dinamarca | 2 / 25 | 0.86 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 2 / 11 | 0.84 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 031 (32/33) a 010 (0/25)
2. Llevar **11 bicis** de 114 (21/23) a 115 (2/25)
3. Llevar **8 bicis** de 116 (22/22) a 008 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

263 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.272 | 0.091 |
| Persistencia | 0.309 | 0.066 |
| Persistencia 0/1 | 0.309 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
