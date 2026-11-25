# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 20:10 (hora de Ciudad de México).

## Último pronóstico: 24/11 20:10 a 21:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · lluvia 1.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.55** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 1.00 | 17-19 |
| 098 Emilio Dondé-Av. Balderas | 28 / 29 | 0.00 | 0.81 | 27-29 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.60 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 23 / 26 | 0.00 | 0.54 | 22-26 |
| 010 Reforma - Ramírez | 2 / 22 | 0.48 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 15 | 0.43 | 0.00 | 1-8 |
| 555 Ribera de San Cosme - Insurg | 22 / 28 | 0.00 | 0.36 | 20-28 |
| 026 Reforma - Versalles | 2 / 14 | 0.24 | 0.00 | 1-7 |
| 086 Sullivan-Insurgentes | 9 / 16 | 0.00 | 0.20 | 8-15 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.18 | 0.00 | 1-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (19/19) a 003 (1/27)
2. Llevar **8 bicis** de 098 (28/29) a 010 (2/22)
3. Llevar **5 bicis** de 450 (23/26) a 113 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

567 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.033 |
| Sin resincronizar | 0.244 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
