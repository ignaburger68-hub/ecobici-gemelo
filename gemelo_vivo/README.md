# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 16:08 (hora de Ciudad de México).

## Último pronóstico: 25/11 16:08 a 17:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.9 °C** · sin lluvia · viento 7 km/h · día hábil

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
| 270 De la República-Ponciano Arr | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 029 Reforma - Bucareli | 0 / 29 | 0.96 | 0.00 | 1-11 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.96 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.96 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 28 | 0.94 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.93 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (20/23) a 270 (0/26)
2. Llevar **11 bicis** de 031 (24/32) a 555 (1/28)
3. Llevar **5 bicis** de 113 (7/15) a 041 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

621 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.241 | 0.080 |
| Persistencia | 0.264 | 0.059 |
| Persistencia 0/1 | 0.264 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
