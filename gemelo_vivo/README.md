# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 18:31 (hora de Ciudad de México).

## Último pronóstico: 22/11 18:31 a 19:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.53** y las **devoluciones por 0.59** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 112 Av. Morelos-Abraham González | 2 / 20 | 0.70 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 1 / 30 | 0.70 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.69 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 30 / 33 | 0.00 | 0.57 | 25-33 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.51 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 2 / 25 | 0.49 | 0.00 | 1-9 |
| 048 Independencia - Azueta | 9 / 11 | 0.01 | 0.48 | 5-11 |
| 008 Reforma - General Prim | 2 / 17 | 0.46 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 5 / 35 | 0.32 | 0.00 | 2-11 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 029 (30/33) a 263 (0/28)
2. Llevar **4 bicis** de 048 (9/11) a 112 (2/20)
3. Llevar **6 bicis** de 041 (17/27) a 114 (2/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

418 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
