# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 14:31 (hora de Ciudad de México).

## Último pronóstico: 18/11 14:31 a 15:31

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
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 0.98 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.98 | 0.01 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.93 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 2 / 8 | 0.87 | 0.03 | 0-3 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.82 | 24-30 |
| 010 Reforma - Ramírez | 2 / 25 | 0.81 | 0.00 | 0-7 |
| 114 Lucerna-Abraham González | 2 / 18 | 0.71 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.70 | 0.00 | 0-8 |
| 107-108 Tolsa-Balderas | 2 / 52 | 0.69 | 0.00 | 0-8 |
| 260 Av. Juárez-Balderas | 2 / 19 | 0.61 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 117 (29/30) a 256 (1/19)
2. Llevar **12 bicis** de 031 (30/33) a 041 (0/23)
3. Llevar **5 bicis** de 026 (9/11) a 020 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

117 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.030 |
| Sin resincronizar | 0.305 | 0.083 |
| Persistencia | 0.341 | 0.059 |
| Persistencia 0/1 | 0.341 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
