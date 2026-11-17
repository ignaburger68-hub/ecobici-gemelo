# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 11:11 (hora de Ciudad de México).

## Último pronóstico: 17/11 11:11 a 12:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.1 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.01 | 0-3 |
| 026 Reforma - Versalles | 9 / 9 | 0.02 | 0.96 | 3-9 |
| 031 Hamburgo - Insurgentes | 0 / 29 | 0.95 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.95 | 9-16 |
| 555 Ribera de San Cosme - Insurg | 3 / 31 | 0.85 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.84 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.83 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 008 (16/16) a 256 (0/18)
2. Llevar **13 bicis** de 107-108 (21/51) a 555 (3/31)
3. Llevar **4 bicis** de 026 (9/9) a 086 (0/7)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

32 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.164 | 0.043 |
| Sin resincronizar | 0.191 | 0.088 |
| Persistencia | 0.302 | 0.093 |
| Persistencia 0/1 | 0.302 | 0.093 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
