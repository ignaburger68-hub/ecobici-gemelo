# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 28/11/2026 08:23 (hora de Ciudad de México).

## Último pronóstico: 28/11 08:23 a 09:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**7.0 °C** · lluvia 1.7 mm/h · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.68** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.797 | 0.897 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | mucho más frío (< −3 °C) | 1.000 | 1.000 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 3 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 1 | 1.00 | 0.00 | 0-0 |
| 008 Reforma - General Prim | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 1 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 0.99 | 13-16 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 18-21 |
| 031 Hamburgo - Insurgentes | 0 / 3 | 0.97 | 0.66 | 1-3 |
| 270 De la República-Ponciano Arr | 0 / 21 | 0.93 | 0.00 | 2-8 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.74 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.54 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (21/21) a 041 (1/28)
2. Llevar **6 bicis** de 086 (16/16) a 012 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

804 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.110 | 0.035 |
| Sin resincronizar | 0.236 | 0.082 |
| Persistencia | 0.238 | 0.059 |
| Persistencia 0/1 | 0.238 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
