# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 15:39 (hora de Ciudad de México).

## Último pronóstico: 25/11 15:39 a 16:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.9 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.82** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 10 | 0.99 | 0.00 | 0-3 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.98 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.94 | 0.00 | 1-10 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.85 | 0.00 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.82 | 0.00 | 0-8 |
| 098 Emilio Dondé-Av. Balderas | 1 / 29 | 0.81 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 1 / 30 | 0.78 | 0.00 | 1-12 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 031 (29/34) a 041 (0/31)
2. Llevar **8 bicis** de 031 (29/34) a 260 (1/20)
3. Llevar **8 bicis** de 116 (18/23) a 270 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

619 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.240 | 0.080 |
| Persistencia | 0.263 | 0.060 |
| Persistencia 0/1 | 0.263 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
