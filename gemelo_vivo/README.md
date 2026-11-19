# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 13:19 (hora de Ciudad de México).

## Último pronóstico: 19/11 13:18 a 14:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.9 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 18 | 1.00 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.01 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.98 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.97 | 9-17 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 114 (17/17) a 270 (0/25)
2. Llevar **10 bicis** de 116 (16/16) a 010 (0/27)
3. Llevar **12 bicis** de 117 (22/27) a 555 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

183 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.037 |
| Sin resincronizar | 0.277 | 0.093 |
| Persistencia | 0.330 | 0.071 |
| Persistencia 0/1 | 0.330 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
