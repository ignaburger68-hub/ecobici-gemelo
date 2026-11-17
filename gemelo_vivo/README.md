# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 12:11 (hora de Ciudad de México).

## Último pronóstico: 17/11 12:11 a 13:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.99 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.98 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.98 | 0.05 | 0-5 |
| 048 Independencia - Azueta | 0 / 10 | 0.97 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.97 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.97 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 20 | 0.95 | 0.00 | 1-7 |
| 041 Reforma - Av. de la Repúblic | 2 / 20 | 0.70 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 2 / 19 | 0.70 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 008 (15/16) a 555 (0/30)
2. Llevar **7 bicis** de 117 (20/30) a 012 (0/15)
3. Llevar **4 bicis** de 026 (7/9) a 020 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

36 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.155 | 0.037 |
| Sin resincronizar | 0.204 | 0.096 |
| Persistencia | 0.298 | 0.084 |
| Persistencia 0/1 | 0.298 | 0.084 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
