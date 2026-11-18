# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 15:14 (hora de Ciudad de México).

## Último pronóstico: 18/11 15:14 a 16:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.1 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 13 | 1.00 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 0 / 8 | 1.00 | 0.02 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.01 | 0-5 |
| 113 General Prim-Versalles | 0 / 8 | 0.99 | 0.03 | 0-4 |
| 107-108 Tolsa-Balderas | 0 / 52 | 0.98 | 0.00 | 0-9 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.98 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 25 | 0.93 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 18 | 0.87 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.84 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.82 | 21-29 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 117 (29/30) a 010 (1/25)
2. Llevar **10 bicis** de 031 (27/32) a 118 (0/13)
3. Llevar **6 bicis** de 119 (19/27) a 048 (0/8)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

120 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.031 |
| Sin resincronizar | 0.303 | 0.084 |
| Persistencia | 0.341 | 0.061 |
| Persistencia 0/1 | 0.341 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
