# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 13:18 (hora de Ciudad de México).

## Último pronóstico: 18/11 13:18 a 14:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 18 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 0.97 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 2 / 52 | 0.87 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.87 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.77 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.76 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.73 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (32/33) a 270 (0/26)
2. Llevar **14 bicis** de 117 (28/30) a 107-108 (2/52)
3. Llevar **7 bicis** de 008 (12/14) a 260 (0/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

112 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.028 |
| Sin resincronizar | 0.306 | 0.082 |
| Persistencia | 0.345 | 0.054 |
| Persistencia 0/1 | 0.345 | 0.054 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
