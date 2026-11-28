# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 28/11/2026 08:38 (hora de Ciudad de México).

## Último pronóstico: 28/11 08:37 a 09:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**7.2 °C** · lluvia 1.3 mm/h · viento 2 km/h · día fin de semana

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
| 012 Río Lerma - Villalongín | 0 / 11 | 0.98 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 0 / 4 | 0.94 | 0.55 | 1-4 |
| 270 De la República-Ponciano Arr | 0 / 20 | 0.93 | 0.00 | 2-9 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.79 | 18-21 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.68 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 086 (16/16) a 041 (1/28)
2. Llevar **6 bicis** de 260 (20/21) a 012 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

805 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
