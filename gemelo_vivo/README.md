# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 18:17 (hora de Ciudad de México).

## Último pronóstico: 22/11 18:16 a 19:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.3 °C** · lluvia 0.7 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.55** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 1 / 22 | 0.86 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 31 / 33 | 0.00 | 0.74 | 27-33 |
| 031 Hamburgo - Insurgentes | 2 / 35 | 0.73 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 9 / 11 | 0.00 | 0.48 | 5-11 |
| 115 Roma-Dinamarca | 2 / 25 | 0.46 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.45 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 2 / 17 | 0.40 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 4 / 18 | 0.39 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 029 (31/33) a 031 (2/35)
2. Llevar **5 bicis** de 048 (9/11) a 114 (1/22)
3. Llevar **6 bicis** de 012 (9/13) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

417 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
