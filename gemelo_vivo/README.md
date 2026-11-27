# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 19:55 (hora de Ciudad de México).

## Último pronóstico: 26/11 19:54 a 20:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.1 °C** · lluvia 0.1 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.78 | 0.96 | 5-5 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.95 | 0.03 | 1-10 |
| 029 Reforma - Bucareli | 31 / 31 | 0.00 | 0.94 | 24-31 |
| 026 Reforma - Versalles | 0 / 13 | 0.94 | 0.01 | 1-8 |
| 256 Gómez Farías-Sadi Carnot | 19 / 20 | 0.00 | 0.91 | 14-20 |
| 041 Reforma - Av. de la Repúblic | 27 / 28 | 0.00 | 0.83 | 21-28 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.80 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.77 | 16-21 |
| 115 Roma-Dinamarca | 1 / 23 | 0.75 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 256 (19/20) a 020 (1/21)
2. Llevar **7 bicis** de 029 (31/31) a 086 (0/14)
3. Llevar **12 bicis** de 041 (27/28) a 115 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

708 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.249 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
