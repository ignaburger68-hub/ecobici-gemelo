# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 22:33 (hora de Ciudad de México).

## Último pronóstico: 25/11 22:33 a 23:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 020 Reforma- Río Támesis | 0 / 22 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 1.00 | 25-27 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 12 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 10 / 10 | 0.05 | 0.98 | 2-9 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.95 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.90 | 12-20 |
| 041 Reforma - Av. de la Repúblic | 31 / 32 | 0.00 | 0.87 | 28-32 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (27/27) a 020 (0/22)
2. Llevar **13 bicis** de 041 (31/32) a 117 (0/28)
3. Llevar **8 bicis** de 260 (20/20) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

648 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
