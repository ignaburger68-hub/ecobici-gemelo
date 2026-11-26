# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 12:03 (hora de Ciudad de México).

## Último pronóstico: 26/11 12:03 a 13:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · lluvia 0.1 mm/h · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 28 / 28 | 0.00 | 1.00 | 24-28 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.89 | 1.00 | 1-1 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.95 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 0 / 11 | 0.81 | 0.46 | 5-11 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.77 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.73 | 16-21 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.72 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 2 / 11 | 0.70 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (28/28) a 010 (0/25)
2. Llevar **12 bicis** de 260 (19/21) a 041 (1/32)
3. Llevar **8 bicis** de 113 (13/15) a 255 (0/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

675 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.035 |
| Sin resincronizar | 0.245 | 0.081 |
| Persistencia | 0.260 | 0.061 |
| Persistencia 0/1 | 0.260 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
