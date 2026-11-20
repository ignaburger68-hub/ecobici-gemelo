# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 18:18 (hora de Ciudad de México).

## Último pronóstico: 19/11 18:18 a 19:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.4 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 16-20 |
| 115 Roma-Dinamarca | 0 / 23 | 1.00 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 27 | 0.98 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 13 | 0.98 | 0.01 | 0-6 |
| 113 General Prim-Versalles | 1 / 14 | 0.92 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.90 | 0.01 | 0-7 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.90 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 2 / 12 | 0.87 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 260 (20/20) a 115 (0/23)
2. Llevar **11 bicis** de 555 (12/29) a 031 (7/32)
3. Llevar **8 bicis** de 116 (15/20) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

204 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.300 | 0.097 |
| Persistencia | 0.335 | 0.069 |
| Persistencia 0/1 | 0.335 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
