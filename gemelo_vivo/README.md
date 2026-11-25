# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 11:08 (hora de Ciudad de México).

## Último pronóstico: 25/11 11:08 a 12:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.98 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 9 | 0.92 | 0.06 | 1-8 |
| 107-108 Tolsa-Balderas | 1 / 57 | 0.89 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.83 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 2 / 22 | 0.80 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.76 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.73 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 3 / 30 | 0.68 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 118 (14/17) a 041 (0/31)
2. Llevar **15 bicis** de 031 (31/34) a 270 (1/26)
3. Llevar **11 bicis** de 115 (22/25) a 107-108 (1/57)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

600 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
