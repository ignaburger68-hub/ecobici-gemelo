# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 01:24 (hora de Ciudad de México).

## Último pronóstico: 25/11 22:47 a 23:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 1.00 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 0 / 25 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 1.00 | 25-27 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 1 / 10 | 0.95 | 0.00 | 0-1 |
| 048 Independencia - Azueta | 10 / 10 | 0.04 | 0.92 | 3-9 |
| 041 Reforma - Av. de la Repúblic | 31 / 32 | 0.00 | 0.70 | 25-32 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (27/27) a 020 (0/22)
2. Llevar **8 bicis** de 041 (31/32) a 026 (1/10)
3. Llevar **9 bicis** de 260 (20/21) a 117 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

653 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.244 | 0.083 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
