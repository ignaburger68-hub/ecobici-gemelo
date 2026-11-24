# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 21:40 (hora de Ciudad de México).

## Último pronóstico: 23/11 21:40 a 22:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 18-21 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.97 | 11-16 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.62 | 9-11 |
| 117 Londres-Nápoles | 1 / 30 | 0.58 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.46 | 28-31 |
| 031 Hamburgo - Insurgentes | 4 / 36 | 0.42 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 2 / 15 | 0.14 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 18 / 21 | 0.00 | 0.13 | 15-20 |
| 555 Ribera de San Cosme - Insurg | 26 / 32 | 0.00 | 0.09 | 23-31 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (16/16) a 031 (4/36)
2. Llevar **8 bicis** de 260 (21/21) a 117 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

502 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.032 |
| Sin resincronizar | 0.249 | 0.088 |
| Persistencia | 0.285 | 0.060 |
| Persistencia 0/1 | 0.285 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
