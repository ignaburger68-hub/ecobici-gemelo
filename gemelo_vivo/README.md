# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 10:56 (hora de Ciudad de México).

## Último pronóstico: 18/11 10:56 a 11:56

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
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 1.00 | 26-30 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 7-11 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 0 / 10 | 0.98 | 0.01 | 0-5 |
| 118 Liverpool-Dinamarca | 12 / 13 | 0.00 | 0.93 | 9-13 |
| 107-108 Tolsa-Balderas | 1 / 54 | 0.92 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.89 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.87 | 29-33 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.84 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.81 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 117 (30/30) a 107-108 (1/54)
2. Llevar **9 bicis** de 118 (12/13) a 256 (1/19)
3. Llevar **8 bicis** de 026 (11/11) a 041 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

102 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.026 |
| Sin resincronizar | 0.310 | 0.084 |
| Persistencia | 0.355 | 0.048 |
| Persistencia 0/1 | 0.355 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
