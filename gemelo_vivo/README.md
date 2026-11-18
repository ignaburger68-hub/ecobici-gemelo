# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 01:42 (hora de Ciudad de México).

## Último pronóstico: 17/11 22:53 a 23:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.99 | 25-27 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 10 | 0.99 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.99 | 0.00 | 0-1 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 15 | 0.99 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 555 (29/29) a 012 (0/14)
2. Llevar **12 bicis** de 450 (27/27) a 031 (0/25)
3. Llevar **6 bicis** de 259 (22/24) a 020 (0/8)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

85 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.324 | 0.093 |
| Persistencia | 0.353 | 0.045 |
| Persistencia 0/1 | 0.353 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
