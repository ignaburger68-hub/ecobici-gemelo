# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 15:58 (hora de Ciudad de México).

## Último pronóstico: 17/11 15:58 a 16:58

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
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-8 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 6 | 0.99 | 0.38 | 1-6 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 18 | 0.98 | 0.01 | 2-11 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.97 | 0.06 | 0-6 |
| 270 De la República-Ponciano Arr | 0 / 24 | 0.96 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.96 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 031 (19/27) a 118 (0/16)
2. Llevar **8 bicis** de 117 (22/30) a 259 (0/24)
3. Llevar **5 bicis** de 031 (19/27) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

52 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.147 | 0.029 |
| Sin resincronizar | 0.249 | 0.094 |
| Persistencia | 0.323 | 0.053 |
| Persistencia 0/1 | 0.323 | 0.053 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
