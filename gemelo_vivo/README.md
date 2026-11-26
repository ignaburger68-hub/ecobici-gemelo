# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 11:49 (hora de Ciudad de México).

## Último pronóstico: 26/11 11:49 a 12:49

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
| 270 De la República-Ponciano Arr | 0 / 1 | 0.90 | 1.00 | 1-1 |
| 117 Londres-Nápoles | 28 / 28 | 0.00 | 0.99 | 24-28 |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 0.99 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.95 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 0 / 8 | 0.85 | 0.75 | 5-8 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.75 | 16-21 |
| 113 General Prim-Versalles | 13 / 15 | 0.00 | 0.71 | 10-15 |
| 026 Reforma - Versalles | 2 / 11 | 0.69 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.61 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (28/28) a 041 (1/32)
2. Llevar **11 bicis** de 260 (19/21) a 255 (0/32)
3. Llevar **6 bicis** de 113 (13/15) a 026 (2/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

674 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
