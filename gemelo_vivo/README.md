# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 15:29 (hora de Ciudad de México).

## Último pronóstico: 23/11 15:29 a 16:29

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.87** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 0 / 11 | 1.00 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 27 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.96 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 26 | 0.93 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.83 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.73 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.71 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 2 / 20 | 0.65 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 031 (23/35) a 026 (0/11)
2. Llevar **12 bicis** de 117 (23/29) a 010 (2/26)
3. Llevar **9 bicis** de 029 (19/34) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

476 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.061 |
| Persistencia 0/1 | 0.291 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
