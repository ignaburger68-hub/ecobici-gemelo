# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 00:59 (hora de Ciudad de México).

## Último pronóstico: 23/11 22:50 a 23:50

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
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.99 | 12-16 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.94 | 7-11 |
| 450 Ramos Arizpe- Av México Teno | 30 / 31 | 0.00 | 0.70 | 29-31 |
| 117 Londres-Nápoles | 1 / 30 | 0.64 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 2 / 16 | 0.34 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.32 | 16-21 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.28 | 18-22 |
| 010 Reforma - Ramírez | 2 / 25 | 0.23 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 30 / 33 | 0.00 | 0.19 | 28-33 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 086 (16/16) a 117 (1/30)
2. Llevar **10 bicis** de 450 (30/31) a 008 (2/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

511 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.245 | 0.087 |
| Persistencia | 0.278 | 0.060 |
| Persistencia 0/1 | 0.278 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
