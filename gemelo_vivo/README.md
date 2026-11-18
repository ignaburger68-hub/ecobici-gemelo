# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 22:10 (hora de Ciudad de México).

## Último pronóstico: 17/11 22:10 a 23:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 1.00 | 25-27 |
| 031 Hamburgo - Insurgentes | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 0 / 23 | 1.00 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-2 |
| 116 Londres-Roma | 0 / 16 | 0.99 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 450 (27/27) a 031 (0/25)
2. Llevar **15 bicis** de 555 (28/29) a 117 (0/29)
3. Llevar **8 bicis** de 259 (21/24) a 026 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

78 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.027 |
| Sin resincronizar | 0.325 | 0.092 |
| Persistencia | 0.370 | 0.047 |
| Persistencia 0/1 | 0.370 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
