# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 13:34 (hora de Ciudad de México).

## Último pronóstico: 23/11 13:34 a 14:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · lluvia 0.1 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.82** y las **devoluciones por 0.87** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.98 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 28 | 0.98 | 0.00 | 1-8 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.88 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 26 | 0.87 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.63 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 3 / 13 | 0.56 | 0.01 | 0-7 |
| 026 Reforma - Versalles | 2 / 12 | 0.56 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (26/29) a 555 (0/28)
2. Llevar **9 bicis** de 450 (13/29) a 041 (0/32)
3. Llevar **8 bicis** de 115 (18/24) a 270 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

468 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.032 |
| Sin resincronizar | 0.253 | 0.087 |
| Persistencia | 0.291 | 0.062 |
| Persistencia 0/1 | 0.291 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
