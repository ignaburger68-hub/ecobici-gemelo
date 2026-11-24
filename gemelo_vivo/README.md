# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 07:36 (hora de Ciudad de México).

## Último pronóstico: 24/11 07:35 a 08:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 107-108 Tolsa-Balderas | 6 / 51 | 0.97 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 32 | 0.90 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 18 / 19 | 0.00 | 0.90 | 14-19 |
| 112 Av. Morelos-Abraham González | 2 / 20 | 0.89 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 6 / 31 | 0.83 | 0.00 | 0-8 |
| 260 Av. Juárez-Balderas | 8 / 18 | 0.80 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.71 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 8 / 12 | 0.00 | 0.66 | 7-12 |
| 259 Tómas Alva Edison-Ponciano A | 7 / 27 | 0.63 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 118 (18/19) a 107-108 (6/51)
2. Llevar **12 bicis** de 263 (24/29) a 086 (0/16)
3. Llevar **7 bicis** de 026 (8/12) a 041 (2/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

514 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.243 | 0.087 |
| Persistencia | 0.276 | 0.060 |
| Persistencia 0/1 | 0.276 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
