# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 22:39 (hora de Ciudad de México).

## Último pronóstico: 17/11 22:38 a 23:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 23 | 1.00 | 0.00 | 0-1 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 30 | 1.00 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 8 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 5 | 1.00 | 0.06 | 0-3 |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.00 | 0-1 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (29/29) a 012 (0/14)
2. Llevar **17 bicis** de 450 (27/27) a 031 (0/25)
3. Llevar **4 bicis** de 259 (21/24) a 086 (0/5)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

80 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.027 |
| Sin resincronizar | 0.327 | 0.092 |
| Persistencia | 0.366 | 0.048 |
| Persistencia 0/1 | 0.366 | 0.048 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
