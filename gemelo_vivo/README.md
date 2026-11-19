# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 09:29 (hora de Ciudad de México).

## Último pronóstico: 19/11 09:29 a 10:29

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.5 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 1.00 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.97 | 9-13 |
| 115 Roma-Dinamarca | 25 / 26 | 0.00 | 0.86 | 20-26 |
| 107-108 Tolsa-Balderas | 2 / 56 | 0.77 | 0.00 | 4-15 |
| 118 Liverpool-Dinamarca | 9 / 12 | 0.00 | 0.76 | 8-12 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 25 | 0.73 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.73 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 12 / 14 | 0.00 | 0.71 | 9-14 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 113 (13/13) a 255 (0/33)
2. Llevar **13 bicis** de 115 (25/26) a 107-108 (2/56)
3. Llevar **6 bicis** de 118 (9/12) a 086 (2/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

167 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.280 | 0.089 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
