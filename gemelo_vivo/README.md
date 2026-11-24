# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 21:25 (hora de Ciudad de México).

## Último pronóstico: 23/11 21:25 a 22:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.99 | 11-16 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.79 | 18-21 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.77 | 9-11 |
| 117 Londres-Nápoles | 1 / 30 | 0.72 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.69 | 29-31 |
| 031 Hamburgo - Insurgentes | 2 / 36 | 0.69 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.45 | 17-22 |
| 008 Reforma - General Prim | 1 / 15 | 0.42 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 30 / 34 | 0.00 | 0.33 | 29-34 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 086 (16/16) a 031 (2/36)
2. Llevar **11 bicis** de 260 (20/21) a 117 (1/30)
3. Llevar **8 bicis** de 450 (29/31) a 008 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

501 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.031 |
| Sin resincronizar | 0.249 | 0.088 |
| Persistencia | 0.285 | 0.060 |
| Persistencia 0/1 | 0.285 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
