# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 10:51 (hora de Ciudad de México).

## Último pronóstico: 27/11 10:51 a 11:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.8 °C** · lluvia 0.6 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.59** y las **devoluciones por 0.68** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.94 | 9-15 |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.92 | 6-11 |
| 107-108 Tolsa-Balderas | 0 / 26 | 0.89 | 0.00 | 4-13 |
| 115 Roma-Dinamarca | 20 / 21 | 0.00 | 0.67 | 13-20 |
| 012 Río Lerma - Villalongín | 11 / 12 | 0.03 | 0.66 | 3-11 |
| 112 Av. Morelos-Abraham González | 2 / 22 | 0.65 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 30 | 0.49 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 3 / 30 | 0.44 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (15/15) a 086 (0/15)
2. Llevar **9 bicis** de 115 (20/21) a 112 (2/22)
3. Llevar **5 bicis** de 048 (11/11) a 041 (3/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

742 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.037 |
| Sin resincronizar | 0.244 | 0.081 |
| Persistencia | 0.250 | 0.062 |
| Persistencia 0/1 | 0.250 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
