# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 01:07 (hora de Ciudad de México).

## Último pronóstico: 26/11 23:00 a 00:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.7 °C** · lluvia 0.4 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.69** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 13 | 1.00 | 0.00 | 0-1 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-1 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.95 | 0.57 | 1-3 |
| 031 Hamburgo - Insurgentes | 1 / 34 | 0.89 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 8 | 0.88 | 0.00 | 0-1 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.75 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 11 | 0.73 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 1 / 27 | 0.68 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 116 (18/21) a 026 (0/13)
2. Llevar **12 bicis** de 450 (17/23) a 020 (0/21)
3. Llevar **11 bicis** de 256 (17/21) a 031 (1/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

725 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.255 | 0.061 |
| Persistencia 0/1 | 0.255 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
