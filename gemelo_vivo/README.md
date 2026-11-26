# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 12:59 (hora de Ciudad de México).

## Último pronóstico: 26/11 12:59 a 13:59

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.99 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 14 / 14 | 0.00 | 0.99 | 9-14 |
| 117 Londres-Nápoles | 28 / 28 | 0.00 | 0.94 | 20-27 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.94 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.93 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 8 | 0.93 | 0.30 | 2-8 |
| 029 Reforma - Bucareli | 0 / 7 | 0.90 | 0.43 | 2-7 |
| 255 José Rosas Moreno-Guillermo  | 1 / 32 | 0.88 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 117 (28/28) a 041 (1/32)
2. Llevar **8 bicis** de 113 (14/14) a 086 (0/15)
3. Llevar **12 bicis** de 114 (21/22) a 256 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

679 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.246 | 0.081 |
| Persistencia | 0.259 | 0.060 |
| Persistencia 0/1 | 0.259 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
