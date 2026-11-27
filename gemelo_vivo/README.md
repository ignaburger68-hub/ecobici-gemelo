# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 18:29 (hora de Ciudad de México).

## Último pronóstico: 26/11 18:29 a 19:29

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
| 008 Reforma - General Prim | 0 / 8 | 1.00 | 0.00 | 0-2 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 19-21 |
| 048 Independencia - Azueta | 8 / 8 | 0.01 | 1.00 | 4-8 |
| 026 Reforma - Versalles | 0 / 11 | 0.98 | 0.03 | 0-7 |
| 113 General Prim-Versalles | 1 / 14 | 0.96 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.94 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 8 | 0.84 | 0.94 | 8-8 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.87 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 21 | 0.80 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (21/21) a 113 (1/14)
2. Llevar **7 bicis** de 048 (8/8) a 008 (0/8)
3. Llevar **11 bicis** de 029 (23/30) a 012 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

702 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.036 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
