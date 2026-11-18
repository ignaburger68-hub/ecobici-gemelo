# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 12:21 (hora de Ciudad de México).

## Último pronóstico: 18/11 12:21 a 13:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 107-108 Tolsa-Balderas | 0 / 53 | 0.99 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 14 / 14 | 0.01 | 0.95 | 7-13 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.93 | 0.00 | 0-1 |
| 255 José Rosas Moreno-Guillermo  | 2 / 31 | 0.88 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.85 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.74 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 2 / 9 | 0.71 | 0.01 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (32/33) a 041 (2/24)
2. Llevar **14 bicis** de 117 (27/30) a 256 (0/19)
3. Llevar **9 bicis** de 115 (20/21) a 107-108 (0/53)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

108 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.027 |
| Sin resincronizar | 0.307 | 0.083 |
| Persistencia | 0.349 | 0.052 |
| Persistencia 0/1 | 0.349 | 0.052 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
