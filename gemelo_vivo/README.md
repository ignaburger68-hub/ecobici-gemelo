# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 13:49 (hora de Ciudad de México).

## Último pronóstico: 18/11 13:48 a 14:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 51 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.98 | 0.00 | 0-8 |
| 008 Reforma - General Prim | 14 / 14 | 0.00 | 0.98 | 8-14 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.96 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.91 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.91 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 1 / 11 | 0.91 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.79 | 6-11 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 008 (14/14) a 107-108 (0/51)
2. Llevar **7 bicis** de 026 (10/11) a 010 (0/24)
3. Llevar **9 bicis** de 115 (18/19) a 041 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

114 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.028 |
| Sin resincronizar | 0.305 | 0.082 |
| Persistencia | 0.344 | 0.055 |
| Persistencia 0/1 | 0.344 | 0.055 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
