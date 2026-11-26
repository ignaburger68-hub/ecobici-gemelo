# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 07:32 (hora de Ciudad de México).

## Último pronóstico: 26/11 07:32 a 08:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 16 | 1.00 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.98 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 35 | 0.97 | 0.00 | 1-10 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.91 | 0.97 | 2-2 |
| 048 Independencia - Azueta | 10 / 10 | 0.05 | 0.97 | 2-9 |
| 555 Ribera de San Cosme - Insurg | 4 / 25 | 0.94 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 0 / 12 | 0.93 | 0.75 | 8-12 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 119 (22/27) a 086 (0/16)
2. Llevar **11 bicis** de 259 (22/24) a 256 (1/21)
3. Llevar **8 bicis** de 118 (11/16) a 041 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

656 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.243 | 0.082 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
