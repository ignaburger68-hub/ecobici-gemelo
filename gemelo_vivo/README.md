# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 15:02 (hora de Ciudad de México).

## Último pronóstico: 17/11 15:01 a 16:01

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
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 9 | 1.00 | 0.01 | 0-4 |
| 115 Roma-Dinamarca | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.99 | 0.01 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.23 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 19 | 0.96 | 0.00 | 0-8 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.95 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 27 | 0.91 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 2 / 18 | 0.89 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 3 / 16 | 0.79 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 117 (20/30) a 115 (0/24)
2. Llevar **8 bicis** de 098 (12/30) a 010 (1/27)
3. Llevar **6 bicis** de 119 (13/25) a 048 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

48 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.031 |
| Sin resincronizar | 0.231 | 0.095 |
| Persistencia | 0.306 | 0.058 |
| Persistencia 0/1 | 0.306 | 0.058 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
