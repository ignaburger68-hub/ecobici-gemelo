# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 07:20 (hora de Ciudad de México).

## Último pronóstico: 25/11 07:20 a 08:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.88** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 0 / 17 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 23 | 0.98 | 0.00 | 1-8 |
| 255 José Rosas Moreno-Guillermo  | 4 / 35 | 0.95 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 14 / 17 | 0.00 | 0.87 | 11-17 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.84 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 23 | 0.83 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 4 / 35 | 0.69 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (14/17) a 086 (0/14)
2. Llevar **15 bicis** de 119 (24/29) a 255 (4/35)
3. Llevar **11 bicis** de 259 (19/24) a 041 (3/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

584 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
