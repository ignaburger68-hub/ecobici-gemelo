# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 16:12 (hora de Ciudad de México).

## Último pronóstico: 23/11 16:11 a 17:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.76** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 0 / 26 | 0.97 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 11 | 0.97 | 0.02 | 0-6 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.81 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 3 / 27 | 0.48 | 0.00 | 1-9 |
| 555 Ribera de San Cosme - Insurg | 2 / 27 | 0.44 | 0.00 | 0-9 |
| 012 Río Lerma - Villalongín | 2 / 14 | 0.40 | 0.00 | 0-7 |
| 256 Gómez Farías-Sadi Carnot | 3 / 21 | 0.32 | 0.00 | 1-8 |
| 020 Reforma- Río Támesis | 2 / 19 | 0.29 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 029 (20/34) a 010 (0/26)
2. Llevar **10 bicis** de 031 (26/35) a 003 (0/26)
3. Llevar **6 bicis** de 450 (10/29) a 118 (1/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

479 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.290 | 0.061 |
| Persistencia 0/1 | 0.290 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
