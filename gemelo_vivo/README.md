# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 21:11 (hora de Ciudad de México).

## Último pronóstico: 21/11 21:11 a 22:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.83 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 15 | 0.78 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.75 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.75 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 16 | 0.59 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 1 / 15 | 0.54 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 2 / 31 | 0.53 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 3 / 21 | 0.33 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 27 | 0.00 | 0.17 | 23-26 |
| 048 Independencia - Azueta | 4 / 11 | 0.12 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 259 (25/27) a 041 (1/32)
2. Llevar **12 bicis** de 450 (26/30) a 010 (1/27)
3. Llevar **9 bicis** de 270 (23/31) a 115 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

358 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
