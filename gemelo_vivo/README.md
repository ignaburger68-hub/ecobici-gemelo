# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 22:36 (hora de Ciudad de México).

## Último pronóstico: 23/11 22:36 a 23:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.4 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 7-11 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.95 | 11-16 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.36 | 28-31 |
| 031 Hamburgo - Insurgentes | 2 / 35 | 0.32 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 16 | 0.23 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.22 | 15-20 |
| 256 Gómez Farías-Sadi Carnot | 19 / 22 | 0.00 | 0.10 | 17-21 |
| 010 Reforma - Ramírez | 3 / 24 | 0.08 | 0.00 | 1-4 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 086 (16/16) a 117 (0/30)
2. Llevar **8 bicis** de 450 (29/31) a 031 (2/35)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

506 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.032 |
| Sin resincronizar | 0.247 | 0.088 |
| Persistencia | 0.282 | 0.060 |
| Persistencia 0/1 | 0.282 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
