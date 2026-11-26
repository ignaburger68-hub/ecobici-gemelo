# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 21:36 (hora de Ciudad de México).

## Último pronóstico: 25/11 21:36 a 22:36

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
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.99 | 25-27 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.99 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 15-21 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 9-11 |
| 029 Reforma - Bucareli | 30 / 30 | 0.00 | 0.98 | 24-30 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.97 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 1 / 25 | 0.92 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.82 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.79 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (27/27) a 086 (0/16)
2. Llevar **13 bicis** de 260 (21/21) a 115 (1/25)
3. Llevar **7 bicis** de 048 (11/11) a 020 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

644 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
