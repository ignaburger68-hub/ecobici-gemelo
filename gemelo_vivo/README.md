# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 08:15 (hora de Ciudad de México).

## Último pronóstico: 26/11 08:15 a 09:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 1 | 0.77 | 1.00 | 1-1 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.86 | 0.98 | 2-2 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.98 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 1 / 25 | 0.97 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 0 / 27 | 0.87 | 0.00 | 5-16 |
| 112 Av. Morelos-Abraham González | 1 / 18 | 0.83 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.81 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 115 (16/25) a 555 (1/25)
2. Llevar **12 bicis** de 260 (19/21) a 086 (1/16)
3. Llevar **7 bicis** de 113 (8/15) a 041 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

659 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.242 | 0.082 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
