# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 09:00 (hora de Ciudad de México).

## Último pronóstico: 22/11 09:00 a 10:00

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
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 26 | 0.97 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 1 / 33 | 0.82 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 2 / 30 | 0.74 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.56 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 2 / 15 | 0.55 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.55 | 20-26 |
| 085 Rosas Moreno - Sullivan | 3 / 15 | 0.52 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 2 / 11 | 0.52 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.50 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 259 (25/26) a 008 (0/17)
2. Llevar **12 bicis** de 555 (20/33) a 041 (2/30)
3. Llevar **10 bicis** de 107-108 (21/58) a 029 (1/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

378 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
