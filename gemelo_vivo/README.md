# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 06:51 (hora de Ciudad de México).

## Último pronóstico: 25/11 06:51 a 07:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 23 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.99 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 0 / 15 | 0.98 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 0 / 15 | 0.95 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 23 | 0.90 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 1 / 28 | 0.71 | 0.00 | 0-7 |
| 116 Londres-Roma | 2 / 23 | 0.54 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 30 | 0.51 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.49 | 6-11 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 119 (27/29) a 086 (1/14)
2. Llevar **4 bicis** de 118 (4/18) a 114 (1/23)
3. Llevar **5 bicis** de 048 (10/11) a 020 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

582 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.239 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
