# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 19:00 (hora de Ciudad de México).

## Último pronóstico: 19/11 19:00 a 20:00

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
| 112 Av. Morelos-Abraham González | 0 / 20 | 1.00 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 15 | 0.98 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.96 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.96 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 2 / 13 | 0.95 | 0.03 | 1-9 |
| 113 General Prim-Versalles | 2 / 14 | 0.95 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 3 / 27 | 0.95 | 0.00 | 1-11 |
| 115 Roma-Dinamarca | 5 / 25 | 0.91 | 0.00 | 3-15 |
| 117 Londres-Nápoles | 2 / 27 | 0.86 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 555 (19/27) a 003 (1/30)
2. Llevar **9 bicis** de 260 (13/20) a 112 (0/20)
3. Llevar **14 bicis** de 098 (18/31) a 010 (3/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

207 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.300 | 0.098 |
| Persistencia | 0.337 | 0.069 |
| Persistencia 0/1 | 0.337 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
