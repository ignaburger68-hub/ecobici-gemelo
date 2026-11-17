# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 16:12 (hora de Ciudad de México).

## Último pronóstico: 17/11 16:12 a 17:12

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 1-7 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 1 / 24 | 0.98 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.97 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.95 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.90 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 2 / 20 | 0.86 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.84 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.83 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 117 (23/30) a 270 (1/24)
2. Llevar **7 bicis** de 119 (13/25) a 115 (0/24)
3. Llevar **7 bicis** de 031 (17/27) a 118 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

53 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.147 | 0.028 |
| Sin resincronizar | 0.254 | 0.093 |
| Persistencia | 0.326 | 0.051 |
| Persistencia 0/1 | 0.326 | 0.051 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
