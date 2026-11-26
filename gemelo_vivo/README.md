# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 06:35 (hora de Ciudad de México).

## Último pronóstico: 26/11 06:35 a 07:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.2 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 20 | 1.00 | 0.00 | 0-2 |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 003 Reforma - Insurgentes | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 0.97 | 0.02 | 0-5 |
| 029 Reforma - Bucareli | 0 / 26 | 0.94 | 0.00 | 3-12 |
| 117 Londres-Nápoles | 0 / 24 | 0.94 | 0.00 | 2-11 |
| 086 Sullivan-Insurgentes | 5 / 16 | 0.84 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 9 / 26 | 0.70 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 32 | 0.63 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 010 (12/25) a 086 (5/16)
2. Llevar **13 bicis** de 450 (25/27) a 555 (9/26)
3. Llevar **6 bicis** de 085 (11/13) a 114 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

653 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.035 |
| Sin resincronizar | 0.244 | 0.083 |
| Persistencia | 0.261 | 0.061 |
| Persistencia 0/1 | 0.261 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
