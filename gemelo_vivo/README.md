# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 22:04 (hora de Ciudad de México).

## Último pronóstico: 26/11 22:04 a 23:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.7 °C** · lluvia 0.8 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.69** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-1 |
| 020 Reforma- Río Támesis | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.99 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.65 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 2 / 13 | 0.58 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 2 / 25 | 0.57 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 11 | 0.55 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 27 / 28 | 0.00 | 0.48 | 23-28 |
| 115 Roma-Dinamarca | 3 / 21 | 0.29 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 029 (27/28) a 010 (0/26)
2. Llevar **8 bicis** de 256 (18/21) a 020 (0/20)
3. Llevar **7 bicis** de 098 (25/31) a 114 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

717 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.037 |
| Sin resincronizar | 0.248 | 0.082 |
| Persistencia | 0.256 | 0.062 |
| Persistencia 0/1 | 0.256 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
