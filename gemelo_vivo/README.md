# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 11:24 (hora de Ciudad de México).

## Último pronóstico: 24/11 11:24 a 12:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · lluvia 0.4 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.98 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.96 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 0 / 10 | 0.95 | 0.01 | 0-6 |
| 118 Liverpool-Dinamarca | 18 / 19 | 0.00 | 0.88 | 16-19 |
| 026 Reforma - Versalles | 12 / 13 | 0.00 | 0.77 | 7-13 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.76 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 13 / 15 | 0.00 | 0.72 | 11-15 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.69 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 118 (18/19) a 041 (0/30)
2. Llevar **8 bicis** de 113 (13/15) a 270 (2/26)
3. Llevar **5 bicis** de 026 (12/13) a 085 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

530 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.085 |
| Persistencia | 0.276 | 0.061 |
| Persistencia 0/1 | 0.276 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
