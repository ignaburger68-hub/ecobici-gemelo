# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 09:03 (hora de Ciudad de México).

## Último pronóstico: 18/11 09:02 a 10:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 22 | 1.00 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 0 / 29 | 1.00 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 10 / 10 | 0.04 | 1.00 | 3-10 |
| 086 Sullivan-Insurgentes | 0 / 10 | 1.00 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 28 | 0.99 | 0.00 | 0-7 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 23 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.99 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 53 | 0.98 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 117 (22/31) a 270 (0/22)
2. Llevar **10 bicis** de 113 (10/10) a 107-108 (1/53)
3. Llevar **11 bicis** de 115 (17/21) a 255 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

94 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.025 |
| Sin resincronizar | 0.317 | 0.087 |
| Persistencia | 0.358 | 0.044 |
| Persistencia 0/1 | 0.358 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
