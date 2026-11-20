# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 11:40 (hora de Ciudad de México).

## Último pronóstico: 20/11 11:39 a 12:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 29 / 29 | 0.00 | 0.99 | 25-29 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.99 | 5-10 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 10-15 |
| 116 Londres-Roma | 21 / 22 | 0.00 | 0.95 | 18-22 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.83 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 18 / 20 | 0.00 | 0.74 | 15-20 |
| 114 Lucerna-Abraham González | 18 / 20 | 0.00 | 0.73 | 16-20 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (29/29) a 555 (0/32)
2. Llevar **10 bicis** de 116 (21/22) a 086 (1/16)
3. Llevar **8 bicis** de 113 (15/15) a 263 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

247 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.278 | 0.091 |
| Persistencia | 0.316 | 0.064 |
| Persistencia 0/1 | 0.316 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
