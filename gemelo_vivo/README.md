# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 07:50 (hora de Ciudad de México).

## Último pronóstico: 24/11 07:50 a 08:50

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 22 | 0.99 | 0.00 | 1-10 |
| 114 Lucerna-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-7 |
| 107-108 Tolsa-Balderas | 3 / 51 | 0.99 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.96 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 32 | 0.91 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 2 / 19 | 0.82 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 2 / 10 | 0.81 | 0.01 | 0-5 |
| 118 Liverpool-Dinamarca | 18 / 19 | 0.00 | 0.80 | 11-18 |
| 260 Av. Juárez-Balderas | 7 / 21 | 0.80 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 118 (18/19) a 107-108 (3/51)
2. Llevar **10 bicis** de 113 (11/15) a 010 (0/22)
3. Llevar **8 bicis** de 026 (8/12) a 086 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

515 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.243 | 0.087 |
| Persistencia | 0.276 | 0.059 |
| Persistencia 0/1 | 0.276 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
