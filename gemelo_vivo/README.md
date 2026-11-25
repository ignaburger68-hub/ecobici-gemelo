# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 21:40 (hora de Ciudad de México).

## Último pronóstico: 24/11 21:39 a 22:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.2 °C** · lluvia 1.2 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.52** y las **devoluciones por 0.59** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 15 | 0.97 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.96 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 28 / 29 | 0.00 | 0.94 | 27-29 |
| 098 Emilio Dondé-Av. Balderas | 29 / 31 | 0.00 | 0.83 | 29-31 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.79 | 0.00 | 0-3 |
| 116 Londres-Roma | 1 / 23 | 0.62 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 21 | 0.00 | 0.52 | 16-21 |
| 555 Ribera de San Cosme - Insurg | 24 / 30 | 0.00 | 0.40 | 22-30 |
| 048 Independencia - Azueta | 8 / 11 | 0.00 | 0.37 | 7-11 |
| 115 Roma-Dinamarca | 4 / 25 | 0.34 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (28/29) a 118 (1/18)
2. Llevar **15 bicis** de 098 (29/31) a 003 (0/28)
3. Llevar **9 bicis** de 555 (24/30) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

573 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.241 | 0.084 |
| Persistencia | 0.270 | 0.061 |
| Persistencia 0/1 | 0.270 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
