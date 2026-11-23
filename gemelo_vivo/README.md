# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 14:46 (hora de Ciudad de México).

## Último pronóstico: 23/11 14:46 a 15:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.89** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 27 | 1.00 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 56 | 0.99 | 0.00 | 0-7 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 28 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 26 | 0.98 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.92 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (25/29) a 010 (1/26)
2. Llevar **8 bicis** de 450 (13/29) a 107-108 (0/56)
3. Llevar **9 bicis** de 031 (19/36) a 260 (2/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

473 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.062 |
| Persistencia 0/1 | 0.291 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
