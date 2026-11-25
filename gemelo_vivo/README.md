# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 09:14 (hora de Ciudad de México).

## Último pronóstico: 25/11 09:14 a 10:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.6 °C** · lluvia 0.2 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.92 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 13 | 0.90 | 0.01 | 2-8 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.86 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 23 / 25 | 0.00 | 0.85 | 19-25 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.85 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 9 / 15 | 0.00 | 0.75 | 10-15 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 115 (23/25) a 086 (0/17)
2. Llevar **12 bicis** de 118 (15/19) a 555 (1/31)
3. Llevar **8 bicis** de 113 (9/15) a 255 (1/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

592 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.238 | 0.082 |
| Persistencia | 0.267 | 0.060 |
| Persistencia 0/1 | 0.267 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
