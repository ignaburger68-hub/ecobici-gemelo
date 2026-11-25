# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 08:18 (hora de Ciudad de México).

## Último pronóstico: 25/11 08:18 a 09:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 1.00 | 14-15 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 17 / 17 | 0.00 | 0.99 | 13-17 |
| 098 Emilio Dondé-Av. Balderas | 0 / 18 | 0.96 | 0.00 | 1-7 |
| 555 Ribera de San Cosme - Insurg | 0 / 27 | 0.96 | 0.00 | 0-9 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.86 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.84 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 2 / 22 | 0.81 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 2 / 15 | 0.75 | 0.01 | 1-9 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 113 (14/15) a 555 (0/27)
2. Llevar **11 bicis** de 118 (17/17) a 003 (0/27)
3. Llevar **12 bicis** de 115 (14/25) a 041 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

588 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.082 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
