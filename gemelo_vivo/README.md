# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 17:21 (hora de Ciudad de México).

## Último pronóstico: 18/11 17:21 a 18:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.01 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.97 | 0.00 | 0-9 |
| 010 Reforma - Ramírez | 2 / 24 | 0.96 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.92 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 10 / 11 | 0.06 | 0.89 | 2-11 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.87 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 12 / 13 | 0.05 | 0.86 | 3-11 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.85 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 2 / 27 | 0.84 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (14/27) a 010 (2/24)
2. Llevar **7 bicis** de 086 (10/11) a 026 (0/11)
3. Llevar **7 bicis** de 012 (12/13) a 020 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

129 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.033 |
| Sin resincronizar | 0.306 | 0.086 |
| Persistencia | 0.341 | 0.065 |
| Persistencia 0/1 | 0.341 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
