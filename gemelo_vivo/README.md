# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 07:06 (hora de Ciudad de México).

## Último pronóstico: 25/11 07:05 a 08:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 0 / 23 | 0.99 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 0 / 15 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 23 | 0.97 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 0 / 13 | 0.95 | 0.00 | 1-7 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.92 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.69 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 5 / 34 | 0.68 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 9 / 17 | 0.00 | 0.65 | 10-17 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 118 (9/17) a 086 (0/14)
2. Llevar **16 bicis** de 119 (26/29) a 041 (1/31)
3. Llevar **12 bicis** de 259 (21/24) a 255 (5/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

583 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.239 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
