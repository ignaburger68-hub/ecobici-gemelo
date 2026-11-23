# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 19:28 (hora de Ciudad de México).

## Último pronóstico: 22/11 19:28 a 20:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.57** y las **devoluciones por 0.63** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.98 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.97 | 25-33 |
| 115 Roma-Dinamarca | 0 / 25 | 0.94 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 26 | 0.82 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 2 / 17 | 0.48 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 2 / 10 | 0.46 | 0.01 | 0-5 |
| 003 Reforma - Insurgentes | 4 / 27 | 0.35 | 0.00 | 1-9 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.29 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 4 / 26 | 0.26 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 029 (33/33) a 086 (0/12)
2. Llevar **7 bicis** de 260 (12/18) a 010 (1/26)
3. Llevar **6 bicis** de 041 (15/26) a 115 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

422 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
