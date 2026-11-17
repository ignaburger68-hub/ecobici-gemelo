# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 16:56 (hora de Ciudad de México).

## Último pronóstico: 17/11 16:56 a 17:56

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
| 031 Hamburgo - Insurgentes | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.98 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.93 | 0.00 | 0-7 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.92 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.87 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 6 | 0.83 | 0.54 | 0-6 |
| 113 General Prim-Versalles | 2 / 10 | 0.81 | 0.01 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.78 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 260 (11/18) a 010 (1/27)
2. Llevar **8 bicis** de 119 (12/25) a 031 (0/26)
3. Llevar **6 bicis** de 555 (12/30) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

56 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.147 | 0.026 |
| Sin resincronizar | 0.268 | 0.093 |
| Persistencia | 0.334 | 0.047 |
| Persistencia 0/1 | 0.334 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
