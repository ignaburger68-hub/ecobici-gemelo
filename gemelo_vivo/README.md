# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 08:29 (hora de Ciudad de México).

## Último pronóstico: 26/11 08:29 a 09:29

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 1.00 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.98 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 3 | 0.87 | 0.95 | 3-3 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.92 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 26 | 0.91 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.90 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 0 / 27 | 0.86 | 0.00 | 4-15 |
| 112 Av. Morelos-Abraham González | 1 / 18 | 0.81 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 113 (11/15) a 086 (1/16)
2. Llevar **14 bicis** de 115 (19/25) a 555 (3/26)
3. Llevar **10 bicis** de 260 (19/21) a 256 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

660 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.242 | 0.082 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
