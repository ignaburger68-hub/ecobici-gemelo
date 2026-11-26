# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 09:54 (hora de Ciudad de México).

## Último pronóstico: 26/11 09:54 a 10:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.8 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 15 | 1.00 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.98 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.98 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.95 | 20-27 |
| 555 Ribera de San Cosme - Insurg | 1 / 26 | 0.94 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 30 | 0.94 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.88 | 0.46 | 2-6 |
| 048 Independencia - Azueta | 1 / 10 | 0.86 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 117 (27/27) a 086 (0/15)
2. Llevar **10 bicis** de 113 (14/15) a 107-108 (0/54)
3. Llevar **12 bicis** de 260 (19/21) a 555 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

666 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.243 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
