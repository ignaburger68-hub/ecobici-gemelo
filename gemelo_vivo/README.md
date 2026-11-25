# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 19:27 (hora de Ciudad de México).

## Último pronóstico: 24/11 19:27 a 20:27

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.9 °C** · lluvia 0.7 mm/h · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.60** y las **devoluciones por 0.67** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 1 / 12 | 0.95 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 21 | 0.94 | 0.00 | 0-8 |
| 119 Turín-Abraham González | 2 / 24 | 0.90 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 25 / 29 | 0.00 | 0.88 | 20-29 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.84 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.81 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.78 | 12-19 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.77 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 27 / 28 | 0.00 | 0.74 | 24-28 |
| 118 Liverpool-Dinamarca | 4 / 18 | 0.74 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 555 (25/29) a 119 (2/24)
2. Llevar **8 bicis** de 260 (18/19) a 026 (1/12)
3. Llevar **11 bicis** de 098 (27/28) a 010 (1/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

564 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
