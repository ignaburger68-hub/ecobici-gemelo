# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 09:15 (hora de Ciudad de México).

## Último pronóstico: 24/11 09:15 a 10:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.88** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 56 | 1.00 | 0.00 | 2-11 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 1-9 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.99 | 12-16 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.99 | 12-15 |
| 270 De la República-Ponciano Arr | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.98 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.97 | 9-13 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 008 (16/16) a 107-108 (0/56)
2. Llevar **11 bicis** de 113 (15/15) a 555 (0/31)
3. Llevar **10 bicis** de 118 (17/18) a 086 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

521 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.241 | 0.086 |
| Persistencia | 0.275 | 0.060 |
| Persistencia 0/1 | 0.275 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
