# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 11:53 (hora de Ciudad de México).

## Último pronóstico: 18/11 11:53 a 12:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 0.99 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 13 / 13 | 0.00 | 0.98 | 6-13 |
| 107-108 Tolsa-Balderas | 0 / 53 | 0.98 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.98 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.98 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.98 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.96 | 14-21 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.96 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 28 / 29 | 0.00 | 0.86 | 24-29 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (28/29) a 255 (0/32)
2. Llevar **11 bicis** de 115 (21/21) a 041 (0/24)
3. Llevar **7 bicis** de 118 (13/13) a 107-108 (0/53)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

106 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.027 |
| Sin resincronizar | 0.307 | 0.083 |
| Persistencia | 0.350 | 0.051 |
| Persistencia 0/1 | 0.350 | 0.051 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
