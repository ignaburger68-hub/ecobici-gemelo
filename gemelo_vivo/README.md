# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 17:21 (hora de Ciudad de México).

## Último pronóstico: 19/11 17:21 a 18:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 13 | 1.00 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 27 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 2 / 32 | 0.98 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 0 / 29 | 0.97 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.97 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 4 / 19 | 0.95 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 18 / 18 | 0.01 | 0.93 | 6-16 |
| 020 Reforma- Río Támesis | 2 / 20 | 0.91 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 114 (18/18) a 031 (2/32)
2. Llevar **9 bicis** de 260 (10/20) a 010 (1/27)
3. Llevar **7 bicis** de 555 (7/26) a 115 (4/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

200 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.298 | 0.096 |
| Persistencia | 0.336 | 0.069 |
| Persistencia 0/1 | 0.336 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
