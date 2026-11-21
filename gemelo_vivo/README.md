# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 14:45 (hora de Ciudad de México).

## Último pronóstico: 21/11 14:45 a 15:45

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.5 °C** · sin lluvia · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.97** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.98 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.97 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.97 | 13-20 |
| 041 Reforma - Av. de la Repúblic | 2 / 29 | 0.83 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.76 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 9 / 10 | 0.03 | 0.67 | 3-10 |
| 116 Londres-Roma | 2 / 23 | 0.64 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 29 / 31 | 0.00 | 0.64 | 22-31 |
| 112 Av. Morelos-Abraham González | 2 / 22 | 0.61 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 3 / 26 | 0.59 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (20/20) a 041 (2/29)
2. Llevar **8 bicis** de 270 (29/31) a 086 (0/15)
3. Llevar **8 bicis** de 555 (31/33) a 012 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

331 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
