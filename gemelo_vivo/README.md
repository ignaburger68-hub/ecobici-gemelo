# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 15:56 (hora de Ciudad de México).

## Último pronóstico: 19/11 15:56 a 16:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.0 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 0 / 10 | 1.00 | 0.01 | 0-5 |
| 115 Roma-Dinamarca | 0 / 21 | 1.00 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 27 | 0.94 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 13 / 13 | 0.01 | 0.94 | 6-13 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.93 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 14 | 0.92 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 13 | 0.92 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (13/13) a 115 (0/21)
2. Llevar **6 bicis** de 107-108 (11/57) a 010 (0/27)
3. Llevar **5 bicis** de 114 (10/17) a 555 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

194 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.292 | 0.095 |
| Persistencia | 0.334 | 0.070 |
| Persistencia 0/1 | 0.334 | 0.070 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
