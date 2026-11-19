# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 13:04 (hora de Ciudad de México).

## Último pronóstico: 19/11 13:04 a 14:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.9 °C** · sin lluvia · viento 4 km/h · día hábil

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
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 1.00 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 1.00 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 9 | 0.98 | 0.03 | 0-5 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.97 | 10-16 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 114 (17/17) a 270 (0/25)
2. Llevar **15 bicis** de 117 (26/27) a 041 (0/24)
3. Llevar **8 bicis** de 113 (11/13) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

182 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.037 |
| Sin resincronizar | 0.276 | 0.093 |
| Persistencia | 0.330 | 0.071 |
| Persistencia 0/1 | 0.330 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
