# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 06:10 (hora de Ciudad de México).

## Último pronóstico: 18/11 06:10 a 07:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 7 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-1 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.99 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-2 |
| 116 Londres-Roma | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 15 | 0.99 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 0 / 23 | 0.98 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (26/27) a 119 (0/25)
2. Llevar **10 bicis** de 107-108 (41/50) a 114 (0/19)
3. Llevar **5 bicis** de 263 (15/27) a 048 (0/7)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

85 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.324 | 0.093 |
| Persistencia | 0.353 | 0.045 |
| Persistencia 0/1 | 0.353 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
