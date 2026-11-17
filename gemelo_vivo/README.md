# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 17:11 (hora de Ciudad de México).

## Último pronóstico: 17/11 17:10 a 18:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.01 | 0-4 |
| 117 Londres-Nápoles | 1 / 30 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.99 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 0 / 6 | 0.99 | 0.55 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 18 | 0.00 | 0.99 | 9-18 |
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.03 | 0-6 |
| 031 Hamburgo - Insurgentes | 1 / 26 | 0.98 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 24 | 0.98 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.98 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (18/18) a 031 (1/26)
2. Llevar **8 bicis** de 555 (11/30) a 117 (1/30)
3. Llevar **7 bicis** de 116 (10/16) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

57 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.148 | 0.027 |
| Sin resincronizar | 0.272 | 0.092 |
| Persistencia | 0.341 | 0.047 |
| Persistencia 0/1 | 0.341 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
