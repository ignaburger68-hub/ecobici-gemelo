# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 16:42 (hora de Ciudad de México).

## Último pronóstico: 17/11 16:42 a 17:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.99 | 0.01 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 24 | 0.98 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 17 | 0.96 | 0.00 | 0-8 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.95 | 0.00 | 0-7 |
| 115 Roma-Dinamarca | 0 / 24 | 0.95 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 1 / 10 | 0.85 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.84 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 260 (9/17) a 010 (3/27)
2. Llevar **5 bicis** de 116 (7/16) a 020 (0/9)
3. Llevar **8 bicis** de 119 (14/25) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

55 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.147 | 0.027 |
| Sin resincronizar | 0.263 | 0.093 |
| Persistencia | 0.334 | 0.049 |
| Persistencia 0/1 | 0.334 | 0.049 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
