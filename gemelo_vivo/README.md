# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 09:00 (hora de Ciudad de México).

## Último pronóstico: 19/11 09:00 a 10:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.5 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 12 | 1.00 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 1.00 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.99 | 0.00 | 0-6 |
| 107-108 Tolsa-Balderas | 1 / 54 | 0.97 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.96 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 25 / 29 | 0.00 | 0.95 | 18-27 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (25/29) a 107-108 (1/54)
2. Llevar **10 bicis** de 113 (11/13) a 270 (2/26)
3. Llevar **14 bicis** de 115 (21/22) a 255 (0/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

165 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.282 | 0.089 |
| Persistencia | 0.332 | 0.067 |
| Persistencia 0/1 | 0.332 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
