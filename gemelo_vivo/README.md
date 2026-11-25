# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 07:34 (hora de Ciudad de México).

## Último pronóstico: 25/11 07:34 a 08:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 17 | 0.98 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 16 / 17 | 0.00 | 0.90 | 12-17 |
| 255 José Rosas Moreno-Guillermo  | 4 / 35 | 0.86 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 2 / 21 | 0.84 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 3 / 14 | 0.82 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.81 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 23 | 0.78 | 0.00 | 0-9 |
| 114 Lucerna-Abraham González | 2 / 23 | 0.69 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (16/17) a 255 (4/35)
2. Llevar **8 bicis** de 270 (24/28) a 086 (3/14)
3. Llevar **11 bicis** de 107-108 (41/57) a 256 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

585 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.083 |
| Persistencia | 0.266 | 0.061 |
| Persistencia 0/1 | 0.266 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
