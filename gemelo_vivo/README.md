# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 11:39 (hora de Ciudad de México).

## Último pronóstico: 18/11 11:39 a 12:39

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
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 1.00 | 25-30 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.96 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.87 | 27-33 |
| 118 Liverpool-Dinamarca | 12 / 13 | 0.00 | 0.83 | 8-13 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.79 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 20 / 21 | 0.00 | 0.70 | 14-21 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.70 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.68 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.66 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 117 (30/30) a 041 (0/24)
2. Llevar **7 bicis** de 031 (32/33) a 012 (1/12)
3. Llevar **6 bicis** de 118 (12/13) a 098 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

105 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.027 |
| Sin resincronizar | 0.308 | 0.084 |
| Persistencia | 0.351 | 0.050 |
| Persistencia 0/1 | 0.351 | 0.050 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
