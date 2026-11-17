# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 12:40 (hora de Ciudad de México).

## Último pronóstico: 17/11 12:40 a 13:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 1.00 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.98 | 0.10 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.91 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.91 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 9 | 0.88 | 0.03 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.87 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.80 | 0.02 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.66 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 4 / 30 | 0.65 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 3 / 31 | 0.62 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (25/30) a 255 (0/27)
2. Llevar **5 bicis** de 026 (8/9) a 041 (1/20)
3. Llevar **7 bicis** de 010 (14/27) a 256 (1/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

38 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.152 | 0.035 |
| Sin resincronizar | 0.203 | 0.100 |
| Persistencia | 0.294 | 0.080 |
| Persistencia 0/1 | 0.294 | 0.080 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
