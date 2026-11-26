# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 17:18 (hora de Ciudad de México).

## Último pronóstico: 26/11 17:18 a 18:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.57** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 16-20 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.97 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.95 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 1 / 24 | 0.91 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 25 | 0.90 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 28 / 30 | 0.00 | 0.88 | 23-30 |
| 555 Ribera de San Cosme - Insurg | 0 / 33 | 0.85 | 0.00 | 1-17 |
| 270 De la República-Ponciano Arr | 0 / 8 | 0.84 | 0.79 | 6-8 |
| 020 Reforma- Río Támesis | 3 / 21 | 0.79 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (20/20) a 119 (1/24)
2. Llevar **17 bicis** de 029 (28/30) a 003 (0/27)
3. Llevar **8 bicis** de 112 (13/14) a 085 (1/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

697 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
