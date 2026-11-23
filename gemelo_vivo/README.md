# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 15:01 (hora de Ciudad de México).

## Último pronóstico: 23/11 15:01 a 16:01

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 27 | 1.00 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 098 Emilio Dondé-Av. Balderas | 0 / 28 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 1 / 24 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.96 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 3 / 12 | 0.93 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.91 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (25/29) a 010 (1/24)
2. Llevar **10 bicis** de 031 (21/36) a 270 (0/27)
3. Llevar **8 bicis** de 029 (16/34) a 026 (3/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

474 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.062 |
| Persistencia 0/1 | 0.291 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
