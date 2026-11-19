# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 10:43 (hora de Ciudad de México).

## Último pronóstico: 19/11 10:42 a 11:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 118 Liverpool-Dinamarca | 14 / 14 | 0.00 | 1.00 | 10-14 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 14 / 14 | 0.00 | 0.98 | 10-14 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.98 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.97 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 25 | 0.96 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.96 | 8-13 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (14/14) a 107-108 (1/57)
2. Llevar **14 bicis** de 117 (26/28) a 256 (0/20)
3. Llevar **9 bicis** de 026 (14/14) a 041 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

172 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.037 |
| Sin resincronizar | 0.276 | 0.091 |
| Persistencia | 0.330 | 0.070 |
| Persistencia 0/1 | 0.330 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
