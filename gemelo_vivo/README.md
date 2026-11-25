# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 18:59 (hora de Ciudad de México).

## Último pronóstico: 24/11 18:59 a 19:59

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.7 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.62** y las **devoluciones por 0.69** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 26 | 1.00 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.97 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 3 / 13 | 0.94 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.94 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.93 | 10-19 |
| 031 Hamburgo - Insurgentes | 1 / 35 | 0.93 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 2 / 26 | 0.93 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 3 / 22 | 0.91 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (19/19) a 117 (0/26)
2. Llevar **14 bicis** de 029 (26/34) a 118 (1/18)
3. Llevar **10 bicis** de 555 (15/28) a 008 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

562 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
