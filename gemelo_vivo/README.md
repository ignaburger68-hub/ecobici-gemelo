# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 07:50 (hora de Ciudad de México).

## Último pronóstico: 18/11 07:50 a 08:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 1.00 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 1-8 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.99 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 7 | 0.99 | 0.01 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.98 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 3 / 5 | 0.96 | 0.31 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 27 | 0.96 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.96 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 1 / 27 | 0.95 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 107-108 (24/49) a 260 (1/18)
2. Llevar **7 bicis** de 263 (10/27) a 555 (3/27)
3. Llevar **3 bicis** de 113 (3/10) a 255 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

89 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.025 |
| Sin resincronizar | 0.316 | 0.090 |
| Persistencia | 0.351 | 0.045 |
| Persistencia 0/1 | 0.351 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
