# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 17:35 (hora de Ciudad de México).

## Último pronóstico: 18/11 17:35 a 18:35

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
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.98 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 8 / 8 | 0.08 | 0.98 | 2-8 |
| 026 Reforma - Versalles | 1 / 10 | 0.97 | 0.01 | 0-3 |
| 010 Reforma - Ramírez | 2 / 25 | 0.94 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 6 / 20 | 0.90 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 2 / 11 | 0.87 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.83 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 7 / 27 | 0.81 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.78 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 555 (16/27) a 115 (6/20)
2. Llevar **7 bicis** de 048 (8/8) a 010 (2/25)
3. Llevar **5 bicis** de 086 (8/11) a 020 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

130 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.033 |
| Sin resincronizar | 0.307 | 0.086 |
| Persistencia | 0.341 | 0.065 |
| Persistencia 0/1 | 0.341 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
