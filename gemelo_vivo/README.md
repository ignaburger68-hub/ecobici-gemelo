# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 16:09 (hora de Ciudad de México).

## Último pronóstico: 24/11 16:09 a 17:09

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.99 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 14 / 14 | 0.00 | 0.99 | 8-14 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.03 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.97 | 7-13 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.90 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 26 | 0.90 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 29 | 0.85 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.84 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (14/14) a 118 (0/16)
2. Llevar **8 bicis** de 026 (13/13) a 270 (0/27)
3. Llevar **12 bicis** de 114 (19/21) a 555 (1/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

550 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.083 |
| Persistencia | 0.272 | 0.060 |
| Persistencia 0/1 | 0.272 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
