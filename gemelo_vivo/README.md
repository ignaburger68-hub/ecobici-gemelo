# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 09:00 (hora de Ciudad de México).

## Último pronóstico: 25/11 09:00 a 10:00

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
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.99 | 11-15 |
| 020 Reforma- Río Támesis | 0 / 18 | 0.99 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.98 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.97 | 0.00 | 0-7 |
| 118 Liverpool-Dinamarca | 18 / 19 | 0.00 | 0.96 | 16-19 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.95 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 0 / 17 | 0.93 | 0.00 | 2-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.91 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 22 / 29 | 0.00 | 0.89 | 22-28 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 113 (14/15) a 555 (0/30)
2. Llevar **19 bicis** de 117 (22/29) a 255 (1/34)
3. Llevar **12 bicis** de 118 (18/19) a 020 (0/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

591 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
