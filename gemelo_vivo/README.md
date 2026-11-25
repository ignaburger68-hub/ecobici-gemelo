# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 17:19 (hora de Ciudad de México).

## Último pronóstico: 25/11 17:19 a 18:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.0 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.97 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 2 / 8 | 0.87 | 0.06 | 0-4 |
| 115 Roma-Dinamarca | 7 / 24 | 0.86 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 2 / 13 | 0.84 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 25 | 0.72 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 116 (18/23) a 115 (7/24)
2. Llevar **9 bicis** de 098 (11/31) a 020 (0/21)
3. Llevar **6 bicis** de 107-108 (7/56) a 085 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

626 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.243 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
