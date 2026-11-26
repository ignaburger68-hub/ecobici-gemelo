# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 20:25 (hora de Ciudad de México).

## Último pronóstico: 25/11 20:25 a 21:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.79** (1,00 = sin efecto).

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
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.99 | 6-10 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 31 / 31 | 0.00 | 0.96 | 24-31 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.93 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.89 | 15-20 |
| 555 Ribera de San Cosme - Insurg | 25 / 26 | 0.00 | 0.89 | 14-25 |
| 008 Reforma - General Prim | 1 / 13 | 0.76 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 450 (27/27) a 003 (0/27)
2. Llevar **10 bicis** de 260 (19/20) a 113 (0/15)
3. Llevar **11 bicis** de 555 (25/26) a 020 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

639 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
