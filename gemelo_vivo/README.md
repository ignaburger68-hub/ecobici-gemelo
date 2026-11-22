# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 22:08 (hora de Ciudad de México).

## Último pronóstico: 21/11 22:08 a 23:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 26 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 16 | 0.71 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.70 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 28 / 30 | 0.00 | 0.37 | 25-30 |
| 010 Reforma - Ramírez | 3 / 26 | 0.24 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 2 / 15 | 0.20 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 27 | 0.00 | 0.20 | 21-27 |
| 086 Sullivan-Insurgentes | 3 / 14 | 0.19 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 4 / 32 | 0.17 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 450 (28/30) a 115 (0/26)
2. Llevar **9 bicis** de 259 (24/27) a 026 (0/15)
3. Llevar **8 bicis** de 270 (22/31) a 003 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

362 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
