# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 19:42 (hora de Ciudad de México).

## Último pronóstico: 22/11 19:42 a 20:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.8 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.96 | 24-32 |
| 010 Reforma - Ramírez | 1 / 26 | 0.85 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 17 | 0.81 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 1 / 25 | 0.74 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.61 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 2 / 11 | 0.52 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 16 / 19 | 0.00 | 0.48 | 11-19 |
| 003 Reforma - Insurgentes | 5 / 26 | 0.34 | 0.00 | 1-10 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.31 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 029 (33/33) a 010 (1/26)
2. Llevar **7 bicis** de 260 (16/19) a 008 (1/17)
3. Llevar **11 bicis** de 259 (17/26) a 115 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

423 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
