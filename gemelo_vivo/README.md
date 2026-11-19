# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 13:33 (hora de Ciudad de México).

## Último pronóstico: 19/11 13:33 a 14:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.99 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 20 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 1 / 27 | 0.98 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 116 (14/16) a 270 (0/25)
2. Llevar **11 bicis** de 117 (19/26) a 555 (0/30)
3. Llevar **9 bicis** de 114 (14/17) a 031 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

184 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.037 |
| Sin resincronizar | 0.278 | 0.093 |
| Persistencia | 0.330 | 0.071 |
| Persistencia 0/1 | 0.330 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
