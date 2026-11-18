# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 20:01 (hora de Ciudad de México).

## Último pronóstico: 17/11 20:01 a 21:01

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.9 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 003 Reforma - Insurgentes | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.13 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 8 | 1.00 | 0.07 | 0-6 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 16 | 1.00 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 9 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 24 | 0.99 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 2 / 30 | 0.99 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 27 | 0.99 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 255 (23/27) a 029 (2/30)
2. Llevar **19 bicis** de 450 (26/27) a 115 (2/24)
3. Llevar **14 bicis** de 270 (19/23) a 003 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

69 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.137 | 0.027 |
| Sin resincronizar | 0.314 | 0.090 |
| Persistencia | 0.374 | 0.046 |
| Persistencia 0/1 | 0.374 | 0.046 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
