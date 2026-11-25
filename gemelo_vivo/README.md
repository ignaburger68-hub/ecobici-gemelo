# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 06:09 (hora de Ciudad de México).

## Último pronóstico: 25/11 06:09 a 07:09

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 0 / 15 | 1.00 | 0.00 | 0-1 |
| 098 Emilio Dondé-Av. Balderas | 0 / 15 | 0.99 | 0.00 | 0-1 |
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 28 | 0.98 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.96 | 8-18 |
| 086 Sullivan-Insurgentes | 2 / 13 | 0.89 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 2 / 23 | 0.68 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.53 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (19/19) a 086 (2/13)
2. Llevar **9 bicis** de 450 (26/27) a 113 (0/15)
3. Llevar **12 bicis** de 119 (27/29) a 114 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

582 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.239 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
