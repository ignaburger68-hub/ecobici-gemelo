# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 15:25 (hora de Ciudad de México).

## Último pronóstico: 24/11 15:25 a 16:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · lluvia 0.7 mm/h · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 14 | 0.98 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 17 | 0.98 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 26 | 0.82 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.79 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.76 | 0.00 | 0-6 |
| 107-108 Tolsa-Balderas | 1 / 55 | 0.76 | 0.00 | 0-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.71 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.69 | 0.03 | 0-6 |
| 029 Reforma - Bucareli | 1 / 34 | 0.66 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 114 (16/21) a 118 (0/17)
2. Llevar **8 bicis** de 031 (23/34) a 008 (0/14)
3. Llevar **9 bicis** de 098 (18/29) a 020 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

547 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
