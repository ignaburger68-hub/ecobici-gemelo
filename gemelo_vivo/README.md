# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 09:12 (hora de Ciudad de México).

## Último pronóstico: 27/11 09:11 a 10:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.1 °C** · lluvia 0.2 mm/h · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 12-15 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.99 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 34 | 0.97 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.90 | 6-10 |
| 118 Liverpool-Dinamarca | 17 / 19 | 0.00 | 0.85 | 15-19 |
| 008 Reforma - General Prim | 10 / 14 | 0.00 | 0.84 | 10-14 |
| 117 Londres-Nápoles | 21 / 30 | 0.00 | 0.84 | 28-30 |
| 107-108 Tolsa-Balderas | 0 / 31 | 0.81 | 0.00 | 3-13 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (21/30) a 555 (0/34)
2. Llevar **12 bicis** de 113 (15/15) a 086 (0/15)
3. Llevar **12 bicis** de 118 (17/19) a 256 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

735 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.252 | 0.061 |
| Persistencia 0/1 | 0.252 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
