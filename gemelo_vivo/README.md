# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 20:25 (hora de Ciudad de México).

## Último pronóstico: 19/11 20:25 a 21:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 0 / 19 | 0.94 | 0.00 | 0-7 |
| 116 Londres-Roma | 1 / 20 | 0.83 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 3 / 29 | 0.81 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 2 / 16 | 0.77 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 17 / 20 | 0.00 | 0.68 | 13-20 |
| 115 Roma-Dinamarca | 2 / 26 | 0.67 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 2 / 16 | 0.66 | 0.01 | 0-7 |
| 026 Reforma - Versalles | 13 / 14 | 0.01 | 0.60 | 7-14 |
| 255 José Rosas Moreno-Guillermo  | 27 / 31 | 0.00 | 0.50 | 24-31 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (17/20) a 003 (3/29)
2. Llevar **10 bicis** de 255 (27/31) a 116 (1/20)
3. Llevar **6 bicis** de 026 (13/14) a 086 (2/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

213 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.296 | 0.097 |
| Persistencia | 0.334 | 0.068 |
| Persistencia 0/1 | 0.334 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
