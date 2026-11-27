# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 21:36 (hora de Ciudad de México).

## Último pronóstico: 26/11 21:35 a 22:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.7 °C** · lluvia 0.8 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 1 | 0.85 | 0.99 | 1-1 |
| 020 Reforma- Río Támesis | 0 / 20 | 0.98 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 9 | 0.98 | 0.01 | 0-4 |
| 010 Reforma - Ramírez | 3 / 26 | 0.67 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 3 / 28 | 0.63 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 2 / 13 | 0.57 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 7 / 9 | 0.00 | 0.52 | 5-9 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 029 (24/28) a 086 (0/14)
2. Llevar **5 bicis** de 048 (7/9) a 085 (0/9)
3. Llevar **8 bicis** de 256 (18/21) a 012 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

715 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.037 |
| Sin resincronizar | 0.248 | 0.082 |
| Persistencia | 0.257 | 0.062 |
| Persistencia 0/1 | 0.257 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
