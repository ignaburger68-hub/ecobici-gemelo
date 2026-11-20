# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 15:59 (hora de Ciudad de México).

## Último pronóstico: 20/11 15:59 a 16:59

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 11 | 0.98 | 0.01 | 0-6 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 0-7 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.97 | 15-22 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.97 | 16-23 |
| 048 Independencia - Azueta | 1 / 9 | 0.92 | 0.05 | 0-7 |
| 031 Hamburgo - Insurgentes | 31 / 32 | 0.00 | 0.91 | 18-29 |
| 010 Reforma - Ramírez | 1 / 25 | 0.84 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.76 | 0.00 | 0-8 |
| 270 De la República-Ponciano Arr | 2 / 25 | 0.71 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (31/32) a 010 (1/25)
2. Llevar **11 bicis** de 116 (22/22) a 270 (2/25)
3. Llevar **7 bicis** de 114 (23/23) a 026 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

265 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.272 | 0.092 |
| Persistencia | 0.309 | 0.066 |
| Persistencia 0/1 | 0.309 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
