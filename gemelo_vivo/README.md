# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 08:06 (hora de Ciudad de México).

## Último pronóstico: 20/11 08:06 a 09:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 086 Sullivan-Insurgentes | 0 / 15 | 1.00 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.98 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 3 / 26 | 0.97 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.96 | 0.00 | 2-12 |
| 026 Reforma - Versalles | 0 / 14 | 0.90 | 0.06 | 1-11 |
| 010 Reforma - Ramírez | 1 / 25 | 0.88 | 0.00 | 0-11 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.79 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 4 / 31 | 0.76 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 116 (10/20) a 555 (3/26)
2. Llevar **9 bicis** de 117 (9/28) a 086 (0/15)
3. Llevar **7 bicis** de 259 (24/25) a 263 (1/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

232 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.286 | 0.093 |
| Persistencia | 0.324 | 0.064 |
| Persistencia 0/1 | 0.324 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
