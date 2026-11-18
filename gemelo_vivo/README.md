# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 19:33 (hora de Ciudad de México).

## Último pronóstico: 17/11 19:33 a 20:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.9 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.73** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 1.00 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 10 | 1.00 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 0 / 25 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 25 | 0.99 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 450 (24/27) a 003 (0/31)
2. Llevar **12 bicis** de 259 (16/24) a 041 (0/20)
3. Llevar **10 bicis** de 260 (14/18) a 029 (4/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

67 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.140 | 0.026 |
| Sin resincronizar | 0.310 | 0.089 |
| Persistencia | 0.372 | 0.045 |
| Persistencia 0/1 | 0.372 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
