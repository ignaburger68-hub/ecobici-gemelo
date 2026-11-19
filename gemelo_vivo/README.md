# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 18:58 (hora de Ciudad de México).

## Último pronóstico: 18/11 18:58 a 19:58

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.2 °C** · lluvia 0.2 mm/h · viento 12 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 21 | 1.00 | 0.00 | 1-7 |
| 118 Liverpool-Dinamarca | 0 / 12 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.99 | 0.01 | 0-5 |
| 008 Reforma - General Prim | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 12 | 0.98 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 27 / 27 | 0.00 | 0.97 | 16-27 |
| 116 Londres-Roma | 2 / 17 | 0.97 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.97 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 8 | 0.96 | 0.08 | 0-5 |
| 026 Reforma - Versalles | 10 / 10 | 0.24 | 0.95 | 1-9 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 555 (27/27) a 115 (0/21)
2. Llevar **12 bicis** de 029 (20/27) a 116 (2/17)
3. Llevar **10 bicis** de 260 (16/18) a 118 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

135 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.308 | 0.086 |
| Persistencia | 0.345 | 0.066 |
| Persistencia 0/1 | 0.345 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
