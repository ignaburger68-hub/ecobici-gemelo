# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 11:43 (hora de Ciudad de México).

## Último pronóstico: 17/11 11:43 a 12:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.01 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 9 / 9 | 0.02 | 0.97 | 4-9 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.96 | 11-16 |
| 086 Sullivan-Insurgentes | 2 / 7 | 0.79 | 0.06 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 4 / 31 | 0.77 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.74 | 0.01 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.71 | 0.00 | 0-7 |
| 256 Gómez Farías-Sadi Carnot | 2 / 19 | 0.64 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 20 | 0.63 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 008 (16/16) a 555 (4/31)
2. Llevar **5 bicis** de 026 (9/9) a 113 (0/10)
3. Llevar **10 bicis** de 117 (22/30) a 263 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

34 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.157 | 0.040 |
| Sin resincronizar | 0.198 | 0.093 |
| Persistencia | 0.301 | 0.091 |
| Persistencia 0/1 | 0.301 | 0.091 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
