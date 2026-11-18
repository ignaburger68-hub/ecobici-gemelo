# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 16:53 (hora de Ciudad de México).

## Último pronóstico: 18/11 16:53 a 17:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 11 / 11 | 0.01 | 0.98 | 5-11 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.96 | 0.00 | 0-7 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.95 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 13 / 13 | 0.01 | 0.93 | 7-13 |
| 086 Sullivan-Insurgentes | 10 / 11 | 0.05 | 0.91 | 5-11 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.87 | 0.01 | 0-5 |
| 119 Turín-Abraham González | 1 / 27 | 0.81 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.72 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 2 / 11 | 0.69 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (10/11) a 010 (0/25)
2. Llevar **5 bicis** de 012 (13/13) a 020 (1/9)
3. Llevar **6 bicis** de 113 (11/11) a 119 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

127 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.032 |
| Sin resincronizar | 0.304 | 0.085 |
| Persistencia | 0.342 | 0.063 |
| Persistencia 0/1 | 0.342 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
