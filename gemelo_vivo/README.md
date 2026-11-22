# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 08:32 (hora de Ciudad de México).

## Último pronóstico: 22/11 08:32 a 09:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.8 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 003 Reforma - Insurgentes | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.91 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 2 / 33 | 0.82 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.80 | 0.00 | 0-4 |
| 116 Londres-Roma | 1 / 22 | 0.74 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 17 | 0.71 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 2 / 11 | 0.56 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 2 / 15 | 0.51 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.49 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 3 / 20 | 0.43 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 259 (24/26) a 041 (1/31)
2. Llevar **11 bicis** de 107-108 (20/58) a 029 (2/33)
3. Llevar **8 bicis** de 098 (14/29) a 003 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

376 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
