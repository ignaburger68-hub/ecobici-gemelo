# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 13:08 (hora de Ciudad de México).

## Último pronóstico: 17/11 13:08 a 14:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.1 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 1.00 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.98 | 0.01 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.93 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.84 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.82 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 3 / 31 | 0.81 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 20 | 0.76 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 4 / 32 | 0.76 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (24/30) a 270 (0/24)
2. Llevar **5 bicis** de 026 (8/9) a 041 (1/20)
3. Llevar **5 bicis** de 116 (12/17) a 255 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

40 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.034 |
| Sin resincronizar | 0.203 | 0.100 |
| Persistencia | 0.287 | 0.073 |
| Persistencia 0/1 | 0.287 | 0.073 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
