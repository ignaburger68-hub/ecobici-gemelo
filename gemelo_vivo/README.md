# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 17:47 (hora de Ciudad de México).

## Último pronóstico: 26/11 17:47 a 18:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.58** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 18-21 |
| 029 Reforma - Bucareli | 29 / 30 | 0.00 | 0.99 | 26-30 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.97 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 34 | 0.94 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 7 / 8 | 0.03 | 0.90 | 4-8 |
| 115 Roma-Dinamarca | 4 / 22 | 0.90 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 2 / 14 | 0.85 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 4 / 9 | 0.83 | 0.04 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 10 | 0.81 | 0.61 | 5-10 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 029 (29/30) a 115 (4/22)
2. Llevar **11 bicis** de 260 (21/21) a 085 (1/13)
3. Llevar **6 bicis** de 048 (7/8) a 012 (2/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

699 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
