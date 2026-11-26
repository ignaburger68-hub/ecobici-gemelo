# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 21:22 (hora de Ciudad de México).

## Último pronóstico: 25/11 21:22 a 22:22

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
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.99 | 8-10 |
| 115 Roma-Dinamarca | 1 / 25 | 0.92 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.85 | 16-21 |
| 450 Ramos Arizpe- Av México Teno | 24 / 26 | 0.00 | 0.84 | 23-26 |
| 029 Reforma - Bucareli | 27 / 28 | 0.00 | 0.80 | 21-28 |
| 259 Tómas Alva Edison-Ponciano A | 22 / 24 | 0.00 | 0.74 | 21-24 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.67 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 2 / 7 | 0.66 | 0.04 | 0-4 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 450 (24/26) a 115 (1/25)
2. Llevar **10 bicis** de 260 (20/21) a 012 (0/14)
3. Llevar **6 bicis** de 048 (10/10) a 086 (3/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

643 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
