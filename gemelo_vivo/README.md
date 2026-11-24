# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 18:47 (hora de Ciudad de México).

## Último pronóstico: 23/11 18:47 a 19:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · lluvia 0.3 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.75** y las **devoluciones por 0.82** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 18 | 1.00 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 0 / 22 | 1.00 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.98 | 0.00 | 0-2 |
| 029 Reforma - Bucareli | 32 / 32 | 0.00 | 0.98 | 23-32 |
| 010 Reforma - Ramírez | 1 / 25 | 0.97 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 029 (32/32) a 119 (0/27)
2. Llevar **15 bicis** de 555 (22/26) a 010 (1/25)
3. Llevar **11 bicis** de 260 (20/20) a 086 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

490 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.253 | 0.087 |
| Persistencia | 0.289 | 0.059 |
| Persistencia 0/1 | 0.289 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
