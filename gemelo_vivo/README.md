# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 09:30 (hora de Ciudad de México).

## Último pronóstico: 21/11 09:30 a 10:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.95** y las **devoluciones por 0.98** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 1 / 29 | 0.86 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.80 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 31 / 32 | 0.00 | 0.79 | 24-32 |
| 115 Roma-Dinamarca | 2 / 27 | 0.53 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.50 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.49 | 0.00 | 1-11 |
| 041 Reforma - Av. de la Repúblic | 4 / 31 | 0.38 | 0.00 | 2-16 |
| 085 Rosas Moreno - Sullivan | 4 / 15 | 0.36 | 0.00 | 0-6 |
| 116 Londres-Roma | 4 / 23 | 0.26 | 0.00 | 1-10 |
| 048 Independencia - Azueta | 3 / 11 | 0.24 | 0.06 | 1-9 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 270 (31/32) a 119 (1/29)
2. Llevar **10 bicis** de 450 (26/29) a 112 (1/22)
3. Llevar **8 bicis** de 256 (17/23) a 020 (3/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

309 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
