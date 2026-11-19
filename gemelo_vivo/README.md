# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 10:11 (hora de Ciudad de México).

## Último pronóstico: 19/11 10:11 a 11:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 1.00 | 10-17 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.99 | 8-13 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.98 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 1 / 10 | 0.92 | 0.01 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.84 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 11 / 14 | 0.00 | 0.78 | 9-14 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.78 | 11-15 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.77 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (13/13) a 048 (1/10)
2. Llevar **10 bicis** de 114 (17/17) a 256 (0/20)
3. Llevar **10 bicis** de 117 (25/29) a 086 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

170 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.036 |
| Sin resincronizar | 0.277 | 0.090 |
| Persistencia | 0.331 | 0.069 |
| Persistencia 0/1 | 0.331 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
