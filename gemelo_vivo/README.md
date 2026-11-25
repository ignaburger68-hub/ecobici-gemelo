# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 22:36 (hora de Ciudad de México).

## Último pronóstico: 24/11 22:36 a 23:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · lluvia 1.0 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.48** y las **devoluciones por 0.55** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | moderada (1-4 mm/h) | 0.804 | 0.846 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 18 | 1.00 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 31 / 31 | 0.00 | 1.00 | 28-31 |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 28 / 28 | 0.00 | 0.99 | 26-28 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.78 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 16 | 0.61 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.49 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.46 | 21-31 |
| 113 General Prim-Versalles | 2 / 15 | 0.41 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 27 / 29 | 0.00 | 0.33 | 20-28 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 450 (28/28) a 115 (0/25)
2. Llevar **8 bicis** de 098 (31/31) a 118 (0/18)
3. Llevar **10 bicis** de 555 (27/29) a 003 (1/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

577 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.240 | 0.084 |
| Persistencia | 0.268 | 0.061 |
| Persistencia 0/1 | 0.268 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
