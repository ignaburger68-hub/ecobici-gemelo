# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 15:39 (hora de Ciudad de México).

## Último pronóstico: 26/11 15:39 a 16:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · lluvia 0.6 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.67** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 11 | 0.98 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 24 | 0.97 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 0 / 5 | 0.85 | 0.95 | 5-5 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.89 | 14-25 |
| 098 Emilio Dondé-Av. Balderas | 1 / 29 | 0.88 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 6 | 0.88 | 0.61 | 3-6 |
| 048 Independencia - Azueta | 1 / 9 | 0.85 | 0.01 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.84 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (27/27) a 010 (1/24)
2. Llevar **10 bicis** de 260 (19/21) a 041 (0/30)
3. Llevar **6 bicis** de 113 (11/14) a 085 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

690 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.248 | 0.081 |
| Persistencia | 0.259 | 0.061 |
| Persistencia 0/1 | 0.259 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
