# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 19:13 (hora de Ciudad de México).

## Último pronóstico: 24/11 19:13 a 20:13

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.7 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 16 | 1.00 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 0 / 26 | 1.00 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 12 | 1.00 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 22 | 0.99 | 0.00 | 1-9 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 13 | 0.97 | 0.01 | 0-6 |
| 031 Hamburgo - Insurgentes | 1 / 35 | 0.96 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 2 / 26 | 0.96 | 0.00 | 1-8 |
| 119 Turín-Abraham González | 3 / 24 | 0.94 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.94 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (17/19) a 010 (1/22)
2. Llevar **19 bicis** de 098 (27/29) a 031 (1/35)
3. Llevar **10 bicis** de 555 (16/29) a 086 (2/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

563 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.244 | 0.084 |
| Persistencia | 0.273 | 0.061 |
| Persistencia 0/1 | 0.273 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
