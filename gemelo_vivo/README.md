# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 22:05 (hora de Ciudad de México).

## Último pronóstico: 25/11 22:05 a 23:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.99 | 25-27 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 7-11 |
| 008 Reforma - General Prim | 0 / 13 | 0.98 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 1 / 28 | 0.90 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.79 | 0.01 | 0-8 |
| 270 De la República-Ponciano Arr | 27 / 28 | 0.00 | 0.77 | 24-28 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.77 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.76 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.73 | 23-26 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 450 (27/27) a 117 (1/28)
2. Llevar **7 bicis** de 041 (30/32) a 086 (1/17)
3. Llevar **6 bicis** de 048 (11/11) a 020 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

646 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.244 | 0.082 |
| Persistencia | 0.262 | 0.061 |
| Persistencia 0/1 | 0.262 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
