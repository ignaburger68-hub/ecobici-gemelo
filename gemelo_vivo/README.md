# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 16:22 (hora de Ciudad de México).

## Último pronóstico: 22/11 16:22 a 17:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.61** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.67 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 31 | 0.67 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 2 / 15 | 0.63 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.58 | 6-11 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.57 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.53 | 0.01 | 0-7 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.47 | 0.00 | 0-8 |
| 119 Turín-Abraham González | 2 / 26 | 0.44 | 0.00 | 0-7 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 26 | 0.00 | 0.43 | 22-26 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 259 (24/26) a 115 (0/25)
2. Llevar **9 bicis** de 270 (20/25) a 555 (2/31)
3. Llevar **5 bicis** de 026 (10/11) a 113 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

409 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
