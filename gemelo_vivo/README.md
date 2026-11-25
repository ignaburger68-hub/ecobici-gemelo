# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 21:54 (hora de Ciudad de México).

## Último pronóstico: 24/11 21:54 a 22:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · lluvia 1.2 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.50** y las **devoluciones por 0.57** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 098 Emilio Dondé-Av. Balderas | 31 / 31 | 0.00 | 1.00 | 29-31 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 28 / 29 | 0.00 | 0.77 | 26-29 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.50 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 3 / 25 | 0.49 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.43 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 7 / 36 | 0.29 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 7 / 16 | 0.24 | 0.01 | 0-9 |
| 116 Londres-Roma | 4 / 23 | 0.23 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 098 (31/31) a 118 (0/18)
2. Llevar **9 bicis** de 450 (28/29) a 113 (0/15)
3. Llevar **10 bicis** de 029 (29/33) a 115 (3/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

574 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.241 | 0.084 |
| Persistencia | 0.269 | 0.061 |
| Persistencia 0/1 | 0.269 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
