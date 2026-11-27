# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 06:04 (hora de Ciudad de México).

## Último pronóstico: 27/11 06:04 a 07:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.4 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 24 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 17 | 0.98 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.97 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 9 | 0.96 | 0.02 | 1-6 |
| 107-108 Tolsa-Balderas | 0 / 15 | 0.90 | 0.01 | 2-10 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.66 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 11 | 0.45 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.26 | 0.00 | 2-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 450 (20/23) a 041 (0/25)
2. Llevar **10 bicis** de 270 (21/28) a 020 (1/21)
3. Llevar **4 bicis** de 256 (18/21) a 003 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

725 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.255 | 0.061 |
| Persistencia 0/1 | 0.255 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
