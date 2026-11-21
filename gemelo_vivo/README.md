# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 19:33 (hora de Ciudad de México).

## Último pronóstico: 20/11 19:33 a 20:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.2 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 12 | 0.98 | 0.01 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.96 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 15 | 0.96 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.94 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 33 / 33 | 0.00 | 0.92 | 20-32 |
| 118 Liverpool-Dinamarca | 3 / 17 | 0.91 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.88 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.87 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.84 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 555 (33/33) a 003 (3/28)
2. Llevar **12 bicis** de 029 (31/32) a 118 (3/17)
3. Llevar **10 bicis** de 260 (17/20) a 256 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

280 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.267 | 0.093 |
| Persistencia | 0.305 | 0.067 |
| Persistencia 0/1 | 0.305 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
