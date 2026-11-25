# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 19:42 (hora de Ciudad de México).

## Último pronóstico: 24/11 19:42 a 20:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · lluvia 1.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.63** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 098 Emilio Dondé-Av. Balderas | 29 / 29 | 0.00 | 1.00 | 27-29 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.99 | 15-19 |
| 026 Reforma - Versalles | 0 / 12 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.89 | 6-10 |
| 555 Ribera de San Cosme - Insurg | 27 / 31 | 0.00 | 0.76 | 24-31 |
| 003 Reforma - Insurgentes | 2 / 27 | 0.60 | 0.00 | 0-9 |
| 118 Liverpool-Dinamarca | 4 / 18 | 0.59 | 0.00 | 0-6 |
| 450 Ramos Arizpe- Av México Teno | 20 / 26 | 0.00 | 0.45 | 20-26 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.29 | 0.00 | 0-10 |
| 086 Sullivan-Insurgentes | 8 / 14 | 0.02 | 0.28 | 5-14 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (19/19) a 026 (0/12)
2. Llevar **11 bicis** de 555 (27/31) a 118 (4/18)
3. Llevar **10 bicis** de 098 (29/29) a 003 (2/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

565 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.244 | 0.084 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
