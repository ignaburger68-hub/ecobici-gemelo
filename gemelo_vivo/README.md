# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 14:57 (hora de Ciudad de México).

## Último pronóstico: 24/11 14:56 a 15:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · lluvia 0.7 mm/h · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 10 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.98 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.94 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 55 | 0.90 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.89 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.84 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.80 | 0.02 | 0-6 |
| 008 Reforma - General Prim | 3 / 15 | 0.71 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (22/27) a 115 (2/26)
2. Llevar **8 bicis** de 114 (17/21) a 048 (0/10)
3. Llevar **8 bicis** de 031 (26/35) a 086 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

545 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
