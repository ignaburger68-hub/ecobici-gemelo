# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 22:03 (hora de Ciudad de México).

## Último pronóstico: 18/11 22:03 a 23:03

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
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 112 Av. Morelos-Abraham González | 19 / 19 | 0.00 | 0.99 | 17-19 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 13 | 0.98 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 11 | 0.97 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.96 | 0.00 | 0-7 |
| 450 Ramos Arizpe- Av México Teno | 22 / 25 | 0.00 | 0.91 | 23-25 |
| 115 Roma-Dinamarca | 1 / 24 | 0.70 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 14 / 31 | 0.00 | 0.67 | 24-31 |
| 118 Liverpool-Dinamarca | 2 / 14 | 0.59 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (14/31) a 117 (0/29)
2. Llevar **18 bicis** de 450 (22/25) a 003 (0/30)
3. Llevar **9 bicis** de 112 (19/19) a 041 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

148 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.034 |
| Sin resincronizar | 0.299 | 0.090 |
| Persistencia | 0.340 | 0.068 |
| Persistencia 0/1 | 0.340 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
