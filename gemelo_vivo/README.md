# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 18:18 (hora de Ciudad de México).

## Último pronóstico: 18/11 18:18 a 19:18

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
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 21 | 1.00 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.01 | 0-3 |
| 010 Reforma - Ramírez | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.01 | 0-3 |
| 119 Turín-Abraham González | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 25 / 26 | 0.00 | 0.98 | 16-26 |
| 048 Independencia - Azueta | 8 / 8 | 0.13 | 0.97 | 1-8 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 555 (25/26) a 031 (7/29)
2. Llevar **7 bicis** de 048 (8/8) a 115 (0/21)
3. Llevar **10 bicis** de 107-108 (13/51) a 117 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

133 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.308 | 0.086 |
| Persistencia | 0.343 | 0.066 |
| Persistencia 0/1 | 0.343 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
