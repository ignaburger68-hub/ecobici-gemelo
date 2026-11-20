# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 19:29 (hora de Ciudad de México).

## Último pronóstico: 19/11 19:29 a 20:29

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · sin lluvia · viento 9 km/h · día hábil

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
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.01 | 0-7 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.99 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.93 | 0.01 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 20 | 0.89 | 0.00 | 0-5 |
| 116 Londres-Roma | 3 / 18 | 0.89 | 0.00 | 0-7 |
| 114 Lucerna-Abraham González | 1 / 19 | 0.87 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 2 / 33 | 0.76 | 0.00 | 0-11 |
| 260 Av. Juárez-Balderas | 17 / 21 | 0.00 | 0.58 | 14-21 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (20/27) a 086 (0/16)
2. Llevar **10 bicis** de 260 (17/21) a 116 (3/18)
3. Llevar **8 bicis** de 256 (17/20) a 008 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

209 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.299 | 0.097 |
| Persistencia | 0.337 | 0.068 |
| Persistencia 0/1 | 0.337 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
