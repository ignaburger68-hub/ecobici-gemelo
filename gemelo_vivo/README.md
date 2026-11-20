# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 18:32 (hora de Ciudad de México).

## Último pronóstico: 19/11 18:32 a 19:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.6 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.76** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 14-20 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 14 | 0.98 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 1 / 32 | 0.98 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.97 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 25 | 0.96 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.91 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 2 / 20 | 0.91 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.88 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (20/20) a 115 (2/25)
2. Llevar **12 bicis** de 555 (14/28) a 031 (1/32)
3. Llevar **11 bicis** de 256 (16/21) a 086 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

205 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.300 | 0.097 |
| Persistencia | 0.336 | 0.069 |
| Persistencia 0/1 | 0.336 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
