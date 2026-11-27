# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 18:44 (hora de Ciudad de México).

## Último pronóstico: 26/11 18:43 a 19:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 18-21 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 29 / 30 | 0.00 | 0.98 | 26-30 |
| 116 Londres-Roma | 22 / 22 | 0.01 | 0.98 | 10-21 |
| 048 Independencia - Azueta | 7 / 8 | 0.02 | 0.96 | 4-8 |
| 270 De la República-Ponciano Arr | 0 / 7 | 0.80 | 0.96 | 7-7 |
| 113 General Prim-Versalles | 1 / 14 | 0.95 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 2 / 9 | 0.93 | 0.02 | 0-5 |
| 112 Av. Morelos-Abraham González | 14 / 15 | 0.00 | 0.90 | 9-15 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (21/21) a 119 (3/23)
2. Llevar **12 bicis** de 029 (29/30) a 113 (1/14)
3. Llevar **9 bicis** de 116 (22/22) a 085 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

703 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
