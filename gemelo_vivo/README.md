# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 22:32 (hora de Ciudad de México).

## Último pronóstico: 18/11 22:32 a 23:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.5 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 13 | 0.99 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 0 / 29 | 0.99 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 14 | 0.98 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 9 / 9 | 0.00 | 0.98 | 5-9 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.93 | 0.00 | 0-1 |
| 112 Av. Morelos-Abraham González | 18 / 19 | 0.00 | 0.75 | 16-19 |
| 114 Lucerna-Abraham González | 1 / 18 | 0.69 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 23 / 25 | 0.00 | 0.68 | 22-25 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 555 (18/29) a 012 (1/14)
2. Llevar **9 bicis** de 450 (23/25) a 020 (0/13)
3. Llevar **10 bicis** de 112 (18/19) a 031 (0/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

150 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.297 | 0.091 |
| Persistencia | 0.339 | 0.069 |
| Persistencia 0/1 | 0.339 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
