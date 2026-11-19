# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 02:22 (hora de Ciudad de México).

## Último pronóstico: 18/11 23:00 a 00:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.5 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 11 | 1.00 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 0 / 13 | 1.00 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 14 | 1.00 | 0.00 | 0-1 |
| 116 Londres-Roma | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 0 / 14 | 0.99 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 25 / 25 | 0.00 | 0.98 | 23-25 |
| 117 Londres-Nápoles | 0 / 29 | 0.97 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 450 (25/25) a 020 (0/13)
2. Llevar **12 bicis** de 112 (18/19) a 119 (0/26)
3. Llevar **9 bicis** de 255 (26/31) a 012 (3/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

156 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.291 | 0.093 |
| Persistencia | 0.334 | 0.069 |
| Persistencia 0/1 | 0.334 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
