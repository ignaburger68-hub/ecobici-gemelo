# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 16:07 (hora de Ciudad de México).

## Último pronóstico: 26/11 16:07 a 17:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · lluvia 0.6 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.56** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 0.99 | 18-21 |
| 029 Reforma - Bucareli | 0 / 4 | 0.82 | 0.99 | 4-4 |
| 113 General Prim-Versalles | 14 / 14 | 0.00 | 0.99 | 9-14 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.01 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.98 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 29 | 0.98 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 2 | 0.89 | 0.97 | 2-2 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 260 (21/21) a 107-108 (0/55)
2. Llevar **9 bicis** de 113 (14/14) a 010 (0/25)
3. Llevar **10 bicis** de 117 (28/28) a 041 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

692 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.249 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
