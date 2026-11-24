# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 19:32 (hora de Ciudad de México).

## Último pronóstico: 23/11 19:32 a 20:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.82** y las **devoluciones por 0.87** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 23 | 0.98 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 27 / 27 | 0.00 | 0.98 | 17-27 |
| 450 Ramos Arizpe- Av México Teno | 28 / 29 | 0.00 | 0.97 | 25-29 |
| 026 Reforma - Versalles | 11 / 11 | 0.02 | 0.97 | 4-10 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.97 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 0 / 13 | 0.94 | 0.01 | 0-6 |
| 117 Londres-Nápoles | 0 / 29 | 0.92 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.92 | 0.00 | 0-9 |
| 008 Reforma - General Prim | 0 / 15 | 0.87 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 555 (27/27) a 118 (1/18)
2. Llevar **16 bicis** de 450 (28/29) a 117 (0/29)
3. Llevar **13 bicis** de 029 (29/31) a 031 (0/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

493 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.252 | 0.087 |
| Persistencia | 0.290 | 0.059 |
| Persistencia 0/1 | 0.290 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
