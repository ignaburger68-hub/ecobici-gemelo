# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 20:11 (hora de Ciudad de México).

## Último pronóstico: 25/11 20:11 a 21:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 1.00 | 24-27 |
| 041 Reforma - Av. de la Repúblic | 31 / 31 | 0.00 | 0.99 | 25-31 |
| 026 Reforma - Versalles | 7 / 7 | 0.03 | 0.99 | 3-7 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.98 | 6-10 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.95 | 18-21 |
| 113 General Prim-Versalles | 0 / 15 | 0.92 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 260 (20/21) a 003 (0/27)
2. Llevar **17 bicis** de 450 (27/27) a 117 (3/29)
3. Llevar **12 bicis** de 041 (31/31) a 020 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

638 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.264 | 0.060 |
| Persistencia 0/1 | 0.264 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
