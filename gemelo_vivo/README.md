# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 21:54 (hora de Ciudad de México).

## Último pronóstico: 23/11 21:54 a 22:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 1 / 30 | 0.58 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.57 | 17-21 |
| 031 Hamburgo - Insurgentes | 3 / 36 | 0.47 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.45 | 9-11 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.33 | 28-31 |
| 086 Sullivan-Insurgentes | 13 / 16 | 0.00 | 0.14 | 8-15 |
| 256 Gómez Farías-Sadi Carnot | 19 / 22 | 0.00 | 0.11 | 16-21 |
| 008 Reforma - General Prim | 2 / 15 | 0.11 | 0.00 | 1-3 |
| 012 Río Lerma - Villalongín | 3 / 15 | 0.10 | 0.00 | 1-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (20/21) a 031 (3/36)
2. Llevar **5 bicis** de 048 (10/11) a 117 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

503 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.032 |
| Sin resincronizar | 0.248 | 0.088 |
| Persistencia | 0.284 | 0.060 |
| Persistencia 0/1 | 0.284 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
