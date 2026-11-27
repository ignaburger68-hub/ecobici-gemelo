# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 10:37 (hora de Ciudad de México).

## Último pronóstico: 27/11 10:37 a 11:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.8 °C** · lluvia 0.6 mm/h · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.62** y las **devoluciones por 0.71** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 10-15 |
| 107-108 Tolsa-Balderas | 0 / 26 | 0.90 | 0.00 | 2-10 |
| 012 Río Lerma - Villalongín | 12 / 13 | 0.01 | 0.85 | 6-13 |
| 118 Liverpool-Dinamarca | 15 / 19 | 0.00 | 0.80 | 15-19 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.77 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 20 / 21 | 0.00 | 0.70 | 15-21 |
| 048 Independencia - Azueta | 10 / 11 | 0.03 | 0.54 | 4-11 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 26 | 0.44 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (15/19) a 086 (0/15)
2. Llevar **8 bicis** de 113 (15/15) a 255 (1/34)
3. Llevar **6 bicis** de 012 (12/13) a 041 (4/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

741 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.036 |
| Sin resincronizar | 0.244 | 0.081 |
| Persistencia | 0.251 | 0.062 |
| Persistencia 0/1 | 0.251 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
