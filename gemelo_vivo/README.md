# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 09:45 (hora de Ciudad de México).

## Último pronóstico: 18/11 09:45 a 10:45

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 10 / 10 | 0.00 | 1.00 | 7-10 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 20 / 20 | 0.00 | 0.99 | 14-20 |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.99 | 17-21 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.98 | 0.00 | 1-15 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 0.98 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 27 | 0.97 | 0.00 | 1-10 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.97 | 8-11 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (10/10) a 086 (0/12)
2. Llevar **12 bicis** de 114 (20/20) a 119 (0/27)
3. Llevar **11 bicis** de 115 (21/21) a 555 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

97 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.026 |
| Sin resincronizar | 0.314 | 0.085 |
| Persistencia | 0.360 | 0.046 |
| Persistencia 0/1 | 0.360 | 0.046 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
