# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 08:58 (hora de Ciudad de México).

## Último pronóstico: 26/11 08:57 a 09:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.3 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 19 | 1.00 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 53 | 0.99 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.89 | 0.99 | 1-1 |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.99 | 0.01 | 0-7 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (26/27) a 107-108 (1/53)
2. Llevar **10 bicis** de 113 (11/15) a 086 (0/16)
3. Llevar **12 bicis** de 118 (18/19) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

662 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.243 | 0.082 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
