# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 15:39 (hora de Ciudad de México).

## Último pronóstico: 24/11 15:39 a 16:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 10 | 0.98 | 0.01 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.95 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 0.92 | 0.00 | 0-8 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.89 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.76 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 1 / 34 | 0.75 | 0.00 | 1-10 |
| 085 Rosas Moreno - Sullivan | 9 / 10 | 0.02 | 0.75 | 4-10 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.74 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.74 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.65 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 085 (9/10) a 118 (1/17)
2. Llevar **12 bicis** de 098 (23/29) a 555 (0/30)
3. Llevar **6 bicis** de 114 (15/21) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

548 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
