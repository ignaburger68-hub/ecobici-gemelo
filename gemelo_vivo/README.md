# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 21:56 (hora de Ciudad de México).

## Último pronóstico: 17/11 21:56 a 22:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 1.00 | 25-27 |
| 114 Lucerna-Abraham González | 0 / 19 | 1.00 | 0.00 | 0-2 |
| 029 Reforma - Bucareli | 0 / 32 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 23 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.00 | 0-2 |
| 116 Londres-Roma | 0 / 16 | 0.99 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 450 (27/27) a 117 (0/28)
2. Llevar **12 bicis** de 555 (24/28) a 029 (0/32)
3. Llevar **11 bicis** de 259 (21/24) a 115 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

77 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.027 |
| Sin resincronizar | 0.324 | 0.093 |
| Persistencia | 0.371 | 0.048 |
| Persistencia 0/1 | 0.371 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
