# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 21:51 (hora de Ciudad de México).

## Último pronóstico: 25/11 21:51 a 22:51

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
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 9-11 |
| 008 Reforma - General Prim | 0 / 13 | 0.99 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 30 / 30 | 0.00 | 0.99 | 26-30 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.98 | 14-21 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 25 | 0.00 | 0.83 | 23-25 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.82 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.81 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.66 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 450 (27/27) a 086 (2/17)
2. Llevar **10 bicis** de 029 (30/30) a 012 (1/15)
3. Llevar **8 bicis** de 260 (21/21) a 008 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

645 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
