# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 22:08 (hora de Ciudad de México).

## Último pronóstico: 24/11 22:08 a 23:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · lluvia 1.2 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.55** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 18 | 1.00 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 30 / 30 | 0.00 | 0.99 | 28-30 |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 13 | 0.87 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.77 | 0.00 | 0-2 |
| 116 Londres-Roma | 3 / 23 | 0.36 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 25 / 28 | 0.00 | 0.32 | 24-28 |
| 048 Independencia - Azueta | 9 / 11 | 0.00 | 0.24 | 5-10 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 098 (30/30) a 118 (0/18)
2. Llevar **7 bicis** de 450 (25/28) a 086 (1/13)
3. Llevar **12 bicis** de 029 (30/32) a 115 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

575 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
