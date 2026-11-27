# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 13:00 (hora de Ciudad de México).

## Último pronóstico: 27/11 13:00 a 14:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.3 °C** · lluvia 5.5 mm/h · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.59** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | fuerte (≥4 mm/h) | 1.000 | 1.000 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.97 | 9-15 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.91 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.80 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 4 / 26 | 0.77 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 2 / 29 | 0.75 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 4 / 13 | 0.53 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 113 (15/15) a 041 (0/29)
2. Llevar **14 bicis** de 114 (20/23) a 555 (0/31)
3. Llevar **7 bicis** de 118 (15/17) a 086 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

751 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.112 | 0.037 |
| Sin resincronizar | 0.242 | 0.081 |
| Persistencia | 0.248 | 0.061 |
| Persistencia 0/1 | 0.248 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
