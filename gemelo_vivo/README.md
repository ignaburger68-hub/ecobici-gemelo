# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 20:54 (hora de Ciudad de México).

## Último pronóstico: 25/11 20:54 a 21:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.2 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 1.00 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.99 | 25-27 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 17-21 |
| 029 Reforma - Bucareli | 28 / 28 | 0.00 | 0.99 | 23-28 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.98 | 7-10 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 22 | 0.96 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 7 | 0.82 | 0.04 | 0-4 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 450 (27/27) a 003 (0/27)
2. Llevar **13 bicis** de 029 (28/28) a 020 (0/21)
3. Llevar **10 bicis** de 260 (21/21) a 012 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

641 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.034 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.263 | 0.060 |
| Persistencia 0/1 | 0.263 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
