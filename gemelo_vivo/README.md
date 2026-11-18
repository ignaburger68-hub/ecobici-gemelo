# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 21:27 (hora de Ciudad de México).

## Último pronóstico: 17/11 21:26 a 22:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.1 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 003 Reforma - Insurgentes | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 29 | 0.99 | 0.00 | 0-1 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 25 | 0.98 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 450 (26/27) a 010 (0/27)
2. Llevar **12 bicis** de 555 (25/29) a 003 (0/31)
3. Llevar **7 bicis** de 259 (20/24) a 026 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

75 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.129 | 0.028 |
| Sin resincronizar | 0.323 | 0.093 |
| Persistencia | 0.371 | 0.049 |
| Persistencia 0/1 | 0.371 | 0.049 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
