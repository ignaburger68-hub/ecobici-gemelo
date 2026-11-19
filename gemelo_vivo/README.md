# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 21:49 (hora de Ciudad de México).

## Último pronóstico: 18/11 21:49 a 22:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 112 Av. Morelos-Abraham González | 19 / 19 | 0.00 | 0.99 | 17-19 |
| 450 Ramos Arizpe- Av México Teno | 23 / 25 | 0.00 | 0.97 | 23-25 |
| 031 Hamburgo - Insurgentes | 2 / 33 | 0.73 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 2 / 14 | 0.70 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 2 / 30 | 0.62 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 24 | 0.58 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 1 / 12 | 0.56 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 14 | 0.54 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 3 / 26 | 0.48 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 450 (23/25) a 117 (0/28)
2. Llevar **12 bicis** de 112 (19/19) a 031 (2/33)
3. Llevar **9 bicis** de 555 (15/31) a 118 (2/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

147 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.034 |
| Sin resincronizar | 0.300 | 0.090 |
| Persistencia | 0.341 | 0.068 |
| Persistencia 0/1 | 0.341 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
