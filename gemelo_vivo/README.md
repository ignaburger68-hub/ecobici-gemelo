# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 15:53 (hora de Ciudad de México).

## Último pronóstico: 26/11 15:53 a 16:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · lluvia 0.6 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.58** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 29 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 9 | 0.98 | 0.02 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 11 | 0.98 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 27 / 27 | 0.00 | 0.97 | 16-26 |
| 029 Reforma - Bucareli | 0 / 5 | 0.82 | 0.97 | 5-5 |
| 270 De la República-Ponciano Arr | 0 / 5 | 0.88 | 0.73 | 3-5 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.81 | 18-21 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (19/21) a 010 (0/25)
2. Llevar **7 bicis** de 113 (12/14) a 085 (0/11)
3. Llevar **11 bicis** de 114 (19/22) a 020 (0/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

691 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
