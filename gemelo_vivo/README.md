# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 11:10 (hora de Ciudad de México).

## Último pronóstico: 18/11 11:10 a 12:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 13 / 13 | 0.00 | 0.99 | 9-13 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.99 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 0.94 | 25-30 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.84 | 28-33 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.78 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.77 | 6-11 |
| 048 Independencia - Azueta | 1 / 10 | 0.76 | 0.01 | 0-5 |
| 114 Lucerna-Abraham González | 2 / 19 | 0.70 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.69 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 118 (13/13) a 256 (0/19)
2. Llevar **16 bicis** de 031 (32/33) a 107-108 (0/54)
3. Llevar **10 bicis** de 117 (30/30) a 114 (2/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

103 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.027 |
| Sin resincronizar | 0.309 | 0.084 |
| Persistencia | 0.355 | 0.048 |
| Persistencia 0/1 | 0.355 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
