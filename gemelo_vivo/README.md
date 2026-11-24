# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 16:23 (hora de Ciudad de México).

## Último pronóstico: 24/11 16:23 a 17:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.01 | 0-9 |
| 114 Lucerna-Abraham González | 21 / 21 | 0.00 | 0.98 | 16-21 |
| 555 Ribera de San Cosme - Insurg | 0 / 28 | 0.98 | 0.00 | 0-8 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.98 | 0.00 | 1-7 |
| 026 Reforma - Versalles | 12 / 12 | 0.01 | 0.97 | 4-12 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.96 | 8-15 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 114 (21/21) a 555 (0/28)
2. Llevar **7 bicis** de 026 (12/12) a 115 (0/26)
3. Llevar **8 bicis** de 113 (15/15) a 003 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

551 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.083 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
