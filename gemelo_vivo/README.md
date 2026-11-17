# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 14:33 (hora de Ciudad de México).

## Último pronóstico: 17/11 14:33 a 15:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 18 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.97 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.97 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 10 / 10 | 0.08 | 0.96 | 2-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.92 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 0.91 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 2 / 26 | 0.90 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 2 / 17 | 0.89 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.89 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 117 (21/29) a 118 (0/16)
2. Llevar **6 bicis** de 113 (10/10) a 256 (1/19)
3. Llevar **6 bicis** de 098 (10/30) a 260 (0/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

46 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.031 |
| Sin resincronizar | 0.227 | 0.095 |
| Persistencia | 0.299 | 0.060 |
| Persistencia 0/1 | 0.299 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
