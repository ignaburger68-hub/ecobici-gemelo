# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 19:14 (hora de Ciudad de México).

## Último pronóstico: 22/11 19:13 a 20:13

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
| 115 Roma-Dinamarca | 0 / 25 | 0.97 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.82 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.72 | 24-33 |
| 010 Reforma - Ramírez | 2 / 26 | 0.64 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 17 | 0.53 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 2 / 11 | 0.49 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 3 / 16 | 0.41 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 4 / 26 | 0.38 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 2 / 20 | 0.37 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 3 / 31 | 0.36 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 029 (32/33) a 115 (0/25)
2. Llevar **6 bicis** de 260 (14/19) a 086 (1/12)
3. Llevar **7 bicis** de 041 (17/27) a 010 (2/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

421 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
