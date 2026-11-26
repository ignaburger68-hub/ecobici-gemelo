# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 21:08 (hora de Ciudad de México).

## Último pronóstico: 25/11 21:08 a 22:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 115 Roma-Dinamarca | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 7 | 0.99 | 0.02 | 0-4 |
| 029 Reforma - Bucareli | 28 / 28 | 0.00 | 0.99 | 23-28 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.98 | 7-10 |
| 450 Ramos Arizpe- Av México Teno | 25 / 26 | 0.00 | 0.93 | 24-26 |
| 270 De la República-Ponciano Arr | 25 / 26 | 0.00 | 0.88 | 19-26 |
| 259 Tómas Alva Edison-Ponciano A | 23 / 24 | 0.00 | 0.84 | 21-24 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.80 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 450 (25/26) a 115 (0/25)
2. Llevar **10 bicis** de 029 (28/28) a 012 (0/14)
3. Llevar **5 bicis** de 270 (25/26) a 026 (0/7)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

642 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.244 | 0.082 |
| Persistencia | 0.263 | 0.061 |
| Persistencia 0/1 | 0.263 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
