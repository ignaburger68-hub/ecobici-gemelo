# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 19:43 (hora de Ciudad de México).

## Último pronóstico: 25/11 19:43 a 20:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 17-21 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.97 | 21-29 |
| 026 Reforma - Versalles | 7 / 7 | 0.07 | 0.97 | 2-7 |
| 450 Ramos Arizpe- Av México Teno | 25 / 27 | 0.00 | 0.94 | 24-27 |
| 113 General Prim-Versalles | 0 / 15 | 0.94 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.93 | 0.01 | 0-7 |
| 048 Independencia - Azueta | 9 / 10 | 0.01 | 0.88 | 5-10 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.74 | 0.00 | 0-8 |
| 008 Reforma - General Prim | 13 / 15 | 0.00 | 0.70 | 10-15 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (21/21) a 117 (1/29)
2. Llevar **15 bicis** de 450 (25/27) a 003 (1/27)
3. Llevar **7 bicis** de 029 (29/29) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

636 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.265 | 0.060 |
| Persistencia 0/1 | 0.265 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
