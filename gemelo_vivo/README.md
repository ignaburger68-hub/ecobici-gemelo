# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 06:25 (hora de Ciudad de México).

## Último pronóstico: 20/11 06:25 a 07:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.1 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.97 | 0.03 | 3-15 |
| 256 Gómez Farías-Sadi Carnot | 2 / 20 | 0.74 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 20 | 0.65 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 8 / 25 | 0.64 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 2 / 11 | 0.57 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 9 / 11 | 0.00 | 0.54 | 6-11 |
| 114 Lucerna-Abraham González | 3 / 21 | 0.50 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 259 (20/25) a 555 (8/25)
2. Llevar **6 bicis** de 012 (9/11) a 256 (2/20)
3. Llevar **4 bicis** de 010 (5/25) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

227 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.035 |
| Sin resincronizar | 0.289 | 0.095 |
| Persistencia | 0.326 | 0.064 |
| Persistencia 0/1 | 0.326 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
