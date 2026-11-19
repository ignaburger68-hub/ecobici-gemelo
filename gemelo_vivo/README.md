# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 11:53 (hora de Ciudad de México).

## Último pronóstico: 19/11 11:53 a 12:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.9 °C** · sin lluvia · viento 4 km/h · día hábil

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
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 14 / 14 | 0.05 | 0.95 | 3-12 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (24/26) a 555 (0/30)
2. Llevar **10 bicis** de 114 (15/17) a 086 (0/16)
3. Llevar **11 bicis** de 107-108 (23/57) a 255 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

177 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.037 |
| Sin resincronizar | 0.273 | 0.092 |
| Persistencia | 0.330 | 0.070 |
| Persistencia 0/1 | 0.330 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
