# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 22:22 (hora de Ciudad de México).

## Último pronóstico: 24/11 22:22 a 23:22

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
| 115 Roma-Dinamarca | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 31 / 31 | 0.00 | 0.99 | 28-31 |
| 113 General Prim-Versalles | 0 / 14 | 0.98 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.74 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 27 / 28 | 0.00 | 0.72 | 25-28 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.52 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 3 / 14 | 0.45 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 25 / 29 | 0.00 | 0.39 | 21-28 |
| 010 Reforma - Ramírez | 4 / 24 | 0.30 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 098 (31/31) a 115 (0/25)
2. Llevar **10 bicis** de 450 (27/28) a 118 (0/18)
3. Llevar **9 bicis** de 555 (25/29) a 113 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

576 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.240 | 0.084 |
| Persistencia | 0.269 | 0.061 |
| Persistencia 0/1 | 0.269 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
