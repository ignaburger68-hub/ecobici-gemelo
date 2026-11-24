# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 22:22 (hora de Ciudad de México).

## Último pronóstico: 23/11 22:22 a 23:22

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
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 30 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 8-11 |
| 031 Hamburgo - Insurgentes | 2 / 35 | 0.67 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.48 | 16-21 |
| 086 Sullivan-Insurgentes | 14 / 16 | 0.00 | 0.35 | 10-16 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.32 | 28-31 |
| 008 Reforma - General Prim | 2 / 16 | 0.20 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 18 / 22 | 0.00 | 0.05 | 15-20 |
| 555 Ribera de San Cosme - Insurg | 24 / 32 | 0.00 | 0.03 | 21-28 |

### Plan recomendado del camión

1. Llevar **6 bicis** de 048 (11/11) a 031 (2/35)
2. Llevar **6 bicis** de 086 (14/16) a 117 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

505 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.032 |
| Sin resincronizar | 0.248 | 0.088 |
| Persistencia | 0.282 | 0.060 |
| Persistencia 0/1 | 0.282 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
