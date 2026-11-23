# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 07:32 (hora de Ciudad de México).

## Último pronóstico: 23/11 07:32 a 08:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 12 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 11 | 1.00 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 16 / 16 | 0.00 | 0.98 | 12-16 |
| 450 Ramos Arizpe- Av México Teno | 0 / 10 | 0.97 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 13 | 0.96 | 0.01 | 2-8 |
| 026 Reforma - Versalles | 0 / 8 | 0.93 | 0.54 | 4-8 |
| 263 Sadi Carnot - Gómez Farias | 3 / 27 | 0.90 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 0 / 15 | 0.88 | 0.26 | 6-15 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (16/16) a 555 (0/31)
2. Llevar **9 bicis** de 098 (14/26) a 086 (0/12)
3. Llevar **6 bicis** de 115 (7/25) a 263 (3/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

443 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.257 | 0.090 |
| Persistencia | 0.294 | 0.065 |
| Persistencia 0/1 | 0.294 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
