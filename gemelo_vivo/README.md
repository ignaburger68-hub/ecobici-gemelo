# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 13:36 (hora de Ciudad de México).

## Último pronóstico: 17/11 13:36 a 14:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.98 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 7 | 0.92 | 0.11 | 0-6 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.86 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 3 / 25 | 0.86 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.78 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 2 / 9 | 0.78 | 0.01 | 0-4 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 116 (12/17) a 118 (0/16)
2. Llevar **9 bicis** de 117 (21/30) a 041 (0/20)
3. Llevar **6 bicis** de 003 (11/31) a 270 (3/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

42 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.151 | 0.032 |
| Sin resincronizar | 0.207 | 0.098 |
| Persistencia | 0.293 | 0.068 |
| Persistencia 0/1 | 0.293 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
