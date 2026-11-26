# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 19:29 (hora de Ciudad de México).

## Último pronóstico: 25/11 19:28 a 20:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · sin lluvia · viento 9 km/h · día hábil

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
| 450 Ramos Arizpe- Av México Teno | 26 / 27 | 0.00 | 1.00 | 25-27 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 18-21 |
| 008 Reforma - General Prim | 15 / 15 | 0.00 | 0.98 | 11-15 |
| 029 Reforma - Bucareli | 29 / 29 | 0.00 | 0.98 | 22-29 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.98 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 0 / 14 | 0.97 | 0.01 | 1-9 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.97 | 0.01 | 0-7 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.97 | 0.01 | 0-7 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.97 | 0.02 | 1-10 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (26/27) a 003 (0/25)
2. Llevar **13 bicis** de 260 (21/21) a 114 (0/21)
3. Llevar **8 bicis** de 029 (29/29) a 113 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

635 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.265 | 0.059 |
| Persistencia 0/1 | 0.265 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
