# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 17:50 (hora de Ciudad de México).

## Último pronóstico: 18/11 17:50 a 18:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 1 / 27 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.97 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.96 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 10 / 10 | 0.45 | 0.94 | 0-7 |
| 115 Roma-Dinamarca | 4 / 21 | 0.94 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 2 / 11 | 0.93 | 0.01 | 0-5 |
| 010 Reforma - Ramírez | 2 / 25 | 0.92 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 7 / 8 | 0.10 | 0.86 | 2-8 |
| 119 Turín-Abraham González | 2 / 27 | 0.83 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 555 (23/27) a 117 (1/27)
2. Llevar **6 bicis** de 048 (7/8) a 115 (4/21)
3. Llevar **6 bicis** de 086 (10/10) a 113 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

131 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.308 | 0.086 |
| Persistencia | 0.342 | 0.065 |
| Persistencia 0/1 | 0.342 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
