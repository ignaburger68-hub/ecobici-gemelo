# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 10:44 (hora de Ciudad de México).

## Último pronóstico: 23/11 10:44 a 11:44

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 18 / 18 | 0.00 | 1.00 | 14-18 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 3 / 33 | 0.78 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 3 / 57 | 0.70 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 2 / 34 | 0.67 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.64 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 23 / 25 | 0.00 | 0.60 | 19-25 |
| 012 Río Lerma - Villalongín | 12 / 15 | 0.00 | 0.57 | 8-15 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.55 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (18/18) a 555 (3/33)
2. Llevar **6 bicis** de 012 (12/15) a 048 (0/11)
3. Llevar **13 bicis** de 115 (23/25) a 107-108 (3/57)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

456 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.255 | 0.088 |
| Persistencia | 0.295 | 0.064 |
| Persistencia 0/1 | 0.295 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
