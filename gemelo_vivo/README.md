# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 13:22 (hora de Ciudad de México).

## Último pronóstico: 17/11 13:22 a 14:22

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
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.97 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 0.96 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 2 / 31 | 0.72 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 116 (14/17) a 555 (0/31)
2. Llevar **12 bicis** de 117 (23/30) a 270 (0/25)
3. Llevar **8 bicis** de 003 (11/31) a 118 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

41 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.033 |
| Sin resincronizar | 0.204 | 0.099 |
| Persistencia | 0.289 | 0.070 |
| Persistencia 0/1 | 0.289 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
