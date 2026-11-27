# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 18:15 (hora de Ciudad de México).

## Último pronóstico: 26/11 18:15 a 19:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.61** y las **devoluciones por 0.67** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 8 / 8 | 0.01 | 1.00 | 4-8 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 19-21 |
| 113 General Prim-Versalles | 0 / 13 | 0.99 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 7 | 0.82 | 0.96 | 7-7 |
| 115 Roma-Dinamarca | 1 / 20 | 0.88 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.86 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 2 / 15 | 0.86 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 24 / 29 | 0.00 | 0.86 | 25-29 |
| 026 Reforma - Versalles | 1 / 9 | 0.82 | 0.09 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (21/21) a 113 (0/13)
2. Llevar **13 bicis** de 029 (24/29) a 115 (1/20)
3. Llevar **7 bicis** de 048 (8/8) a 012 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

701 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
