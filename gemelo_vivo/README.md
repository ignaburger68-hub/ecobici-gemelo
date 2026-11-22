# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 09:57 (hora de Ciudad de México).

## Último pronóstico: 22/11 09:57 a 10:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.4 °C** · sin lluvia · viento 0 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.98 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 1 / 26 | 0.80 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 4 / 29 | 0.67 | 0.00 | 0-9 |
| 008 Reforma - General Prim | 2 / 17 | 0.66 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.65 | 21-26 |
| 026 Reforma - Versalles | 2 / 14 | 0.65 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 2 / 27 | 0.64 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 259 (25/26) a 020 (0/22)
2. Llevar **10 bicis** de 107-108 (22/59) a 260 (0/19)
3. Llevar **8 bicis** de 098 (13/30) a 085 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

382 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
