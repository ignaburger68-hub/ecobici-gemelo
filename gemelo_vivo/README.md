# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 15:53 (hora de Ciudad de México).

## Último pronóstico: 24/11 15:53 a 16:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · lluvia 0.3 mm/h · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.02 | 0-6 |
| 118 Liverpool-Dinamarca | 0 / 17 | 0.98 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.97 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.97 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.86 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.81 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.73 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 1 / 24 | 0.69 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.63 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 114 (16/21) a 118 (0/17)
2. Llevar **6 bicis** de 026 (12/13) a 003 (0/27)
3. Llevar **13 bicis** de 098 (23/29) a 555 (1/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

549 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
