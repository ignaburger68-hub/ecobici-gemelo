# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 08:46 (hora de Ciudad de México).

## Último pronóstico: 19/11 08:46 a 09:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.5 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 1.00 | 0.00 | 0-1 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 1.00 | 0.00 | 0-1 |
| 041 Reforma - Av. de la Repúblic | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 12 | 1.00 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.99 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 2 / 53 | 0.99 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (18/29) a 270 (0/25)
2. Llevar **13 bicis** de 115 (18/22) a 107-108 (2/53)
3. Llevar **8 bicis** de 114 (8/18) a 555 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

164 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.282 | 0.089 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
