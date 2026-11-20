# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 08:35 (hora de Ciudad de México).

## Último pronóstico: 20/11 08:34 a 09:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 32 | 0.98 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 11 | 0.98 | 0.02 | 0-7 |
| 113 General Prim-Versalles | 9 / 15 | 0.00 | 0.95 | 12-15 |
| 041 Reforma - Av. de la Repúblic | 1 / 30 | 0.89 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 5 / 34 | 0.83 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 116 (18/22) a 555 (2/30)
2. Llevar **9 bicis** de 113 (9/15) a 086 (0/13)
3. Llevar **14 bicis** de 117 (18/29) a 255 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

234 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.286 | 0.093 |
| Persistencia | 0.324 | 0.063 |
| Persistencia 0/1 | 0.324 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
