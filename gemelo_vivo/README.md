# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 11:08 (hora de Ciudad de México).

## Último pronóstico: 22/11 11:08 a 12:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 30 | 0.98 | 0.00 | 0-7 |
| 029 Reforma - Bucareli | 0 / 34 | 0.97 | 0.00 | 0-9 |
| 010 Reforma - Ramírez | 1 / 27 | 0.96 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 12 | 0.95 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.93 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.92 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.92 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 107-108 (24/58) a 041 (1/30)
2. Llevar **15 bicis** de 259 (24/26) a 010 (1/27)
3. Llevar **13 bicis** de 270 (24/30) a 020 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

387 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
