# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 18:31 (hora de Ciudad de México).

## Último pronóstico: 25/11 18:31 a 19:31

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · sin lluvia · viento 9 km/h · día hábil

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
| 008 Reforma - General Prim | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 29 | 0.99 | 0.00 | 0-9 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.99 | 16-21 |
| 029 Reforma - Bucareli | 28 / 29 | 0.00 | 0.98 | 25-29 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.97 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.97 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 9 / 10 | 0.01 | 0.96 | 5-10 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 029 (28/29) a 031 (0/29)
2. Llevar **16 bicis** de 260 (20/21) a 020 (0/21)
3. Llevar **14 bicis** de 555 (16/27) a 117 (2/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

631 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.245 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
