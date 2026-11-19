# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 19:55 (hora de Ciudad de México).

## Último pronóstico: 18/11 19:55 a 20:55

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 17 | 0.99 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 13 | 0.99 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 0 / 28 | 0.98 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.94 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 0 / 21 | 0.94 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.94 | 0.01 | 1-6 |
| 086 Sullivan-Insurgentes | 1 / 9 | 0.93 | 0.04 | 0-5 |
| 119 Turín-Abraham González | 1 / 26 | 0.89 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 11 | 0.85 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (17/18) a 117 (0/28)
2. Llevar **11 bicis** de 255 (22/30) a 116 (0/17)
3. Llevar **10 bicis** de 555 (21/27) a 115 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

139 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.305 | 0.086 |
| Persistencia | 0.346 | 0.067 |
| Persistencia 0/1 | 0.346 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
