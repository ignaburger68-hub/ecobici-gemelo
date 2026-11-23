# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 11:41 (hora de Ciudad de México).

## Último pronóstico: 23/11 11:41 a 12:41

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.6 °C** · lluvia 0.2 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 0 / 11 | 0.96 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 0 / 56 | 0.88 | 0.00 | 0-8 |
| 118 Liverpool-Dinamarca | 17 / 18 | 0.00 | 0.82 | 14-18 |
| 026 Reforma - Versalles | 13 / 14 | 0.00 | 0.78 | 10-14 |
| 555 Ribera de San Cosme - Insurg | 3 / 30 | 0.72 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.70 | 0.00 | 0-8 |
| 255 José Rosas Moreno-Guillermo  | 2 / 34 | 0.68 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (17/18) a 555 (3/30)
2. Llevar **7 bicis** de 026 (13/14) a 086 (0/14)
3. Llevar **10 bicis** de 115 (23/24) a 263 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

460 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.254 | 0.088 |
| Persistencia | 0.293 | 0.064 |
| Persistencia 0/1 | 0.293 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
