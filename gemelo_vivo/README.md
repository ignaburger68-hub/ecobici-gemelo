# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 22:19 (hora de Ciudad de México).

## Último pronóstico: 25/11 22:19 a 23:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 10 / 10 | 0.03 | 0.98 | 3-9 |
| 270 De la República-Ponciano Arr | 27 / 27 | 0.00 | 0.98 | 22-27 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.96 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.96 | 14-21 |
| 450 Ramos Arizpe- Av México Teno | 26 / 27 | 0.00 | 0.88 | 25-27 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 041 (31/32) a 117 (0/28)
2. Llevar **13 bicis** de 450 (26/27) a 020 (0/22)
3. Llevar **13 bicis** de 270 (27/27) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

647 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.244 | 0.082 |
| Persistencia | 0.262 | 0.061 |
| Persistencia 0/1 | 0.262 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
