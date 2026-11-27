# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 18:01 (hora de Ciudad de México).

## Último pronóstico: 26/11 18:01 a 19:01

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.59** y las **devoluciones por 0.65** (1,00 = sin efecto).

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
| 012 Río Lerma - Villalongín | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 8 / 8 | 0.01 | 0.99 | 5-8 |
| 029 Reforma - Bucareli | 30 / 30 | 0.00 | 0.98 | 27-30 |
| 008 Reforma - General Prim | 2 / 9 | 0.97 | 0.00 | 0-2 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.92 | 12-22 |
| 115 Roma-Dinamarca | 4 / 22 | 0.88 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 0 / 9 | 0.87 | 0.83 | 7-9 |
| 113 General Prim-Versalles | 4 / 14 | 0.70 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (21/21) a 012 (0/15)
2. Llevar **16 bicis** de 029 (30/30) a 115 (4/22)
3. Llevar **6 bicis** de 048 (8/8) a 008 (2/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

700 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
