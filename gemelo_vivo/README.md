# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 09:46 (hora de Ciudad de México).

## Último pronóstico: 21/11 09:46 a 10:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 0.99** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 1 / 29 | 0.82 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 30 / 31 | 0.00 | 0.82 | 22-31 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.81 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 27 | 0.73 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.67 | 0.00 | 1-10 |
| 086 Sullivan-Insurgentes | 3 / 17 | 0.37 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 4 / 15 | 0.32 | 0.00 | 0-7 |
| 116 Londres-Roma | 4 / 23 | 0.31 | 0.00 | 0-10 |
| 041 Reforma - Av. de la Repúblic | 6 / 32 | 0.25 | 0.00 | 2-18 |
| 048 Independencia - Azueta | 3 / 11 | 0.24 | 0.06 | 1-9 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 270 (30/31) a 119 (1/29)
2. Llevar **9 bicis** de 256 (17/22) a 112 (1/22)
3. Llevar **8 bicis** de 450 (27/30) a 020 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

310 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
