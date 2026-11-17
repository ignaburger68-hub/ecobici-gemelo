# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 14:05 (hora de Ciudad de México).

## Último pronóstico: 17/11 14:05 a 15:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.17 | 0-6 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.98 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.97 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 0 / 18 | 0.97 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 1 / 32 | 0.95 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 27 | 0.93 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.93 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 27 | 0.87 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.86 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 117 (24/30) a 555 (1/31)
2. Llevar **5 bicis** de 116 (7/17) a 012 (1/15)
3. Llevar **5 bicis** de 117 (24/30) a 029 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

44 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.151 | 0.031 |
| Sin resincronizar | 0.216 | 0.097 |
| Persistencia | 0.298 | 0.063 |
| Persistencia 0/1 | 0.298 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
