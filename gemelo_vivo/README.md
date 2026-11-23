# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 08:00 (hora de Ciudad de México).

## Último pronóstico: 23/11 08:00 a 09:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 0 / 13 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 26 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 17 | 0.98 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 0 / 14 | 0.97 | 0.00 | 1-5 |
| 086 Sullivan-Insurgentes | 2 / 11 | 0.94 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 2 / 27 | 0.94 | 0.00 | 0-1 |
| 107-108 Tolsa-Balderas | 6 / 56 | 0.93 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 010 (21/26) a 555 (0/31)
2. Llevar **9 bicis** de 117 (9/30) a 012 (0/13)
3. Llevar **9 bicis** de 115 (9/25) a 107-108 (6/56)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

445 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.256 | 0.090 |
| Persistencia | 0.293 | 0.065 |
| Persistencia 0/1 | 0.293 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
