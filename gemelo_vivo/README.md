# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 19:56 (hora de Ciudad de México).

## Último pronóstico: 24/11 19:56 a 20:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · lluvia 1.1 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.52** y las **devoluciones por 0.59** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.85 | 16-19 |
| 098 Emilio Dondé-Av. Balderas | 28 / 29 | 0.00 | 0.84 | 27-29 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.72 | 7-11 |
| 450 Ramos Arizpe- Av México Teno | 23 / 26 | 0.00 | 0.57 | 22-26 |
| 026 Reforma - Versalles | 1 / 13 | 0.53 | 0.00 | 1-7 |
| 555 Ribera de San Cosme - Insurg | 26 / 31 | 0.00 | 0.47 | 23-31 |
| 113 General Prim-Versalles | 2 / 15 | 0.31 | 0.00 | 0-7 |
| 029 Reforma - Bucareli | 29 / 33 | 0.00 | 0.29 | 25-33 |
| 003 Reforma - Insurgentes | 2 / 27 | 0.24 | 0.00 | 1-8 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.20 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (18/19) a 003 (2/27)
2. Llevar **5 bicis** de 098 (28/29) a 026 (1/13)
3. Llevar **5 bicis** de 048 (10/11) a 113 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

566 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
