# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 09:33 (hora de Ciudad de México).

## Último pronóstico: 23/11 09:33 a 10:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.98 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 0 / 16 | 0.96 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.92 | 0.00 | 0-10 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.89 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 3 / 27 | 0.88 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.85 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 0 / 17 | 0.85 | 0.00 | 3-10 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 117 (29/31) a 010 (3/27)
2. Llevar **11 bicis** de 115 (21/24) a 256 (0/22)
3. Llevar **5 bicis** de 113 (10/15) a 048 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

451 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.257 | 0.089 |
| Persistencia | 0.295 | 0.064 |
| Persistencia 0/1 | 0.295 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
