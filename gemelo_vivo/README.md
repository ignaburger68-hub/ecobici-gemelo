# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 19:47 (hora de Ciudad de México).

## Último pronóstico: 17/11 19:47 a 20:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.9 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 15 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 6 | 1.00 | 0.11 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 19 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.99 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 10 | 0.98 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 0.98 | 0.02 | 0-2 |
| 029 Reforma - Bucareli | 3 / 31 | 0.98 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 0 / 24 | 0.98 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.97 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 24 | 0.96 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 450 (26/27) a 029 (3/31)
2. Llevar **16 bicis** de 255 (23/27) a 003 (1/31)
3. Llevar **10 bicis** de 260 (15/17) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

68 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.138 | 0.026 |
| Sin resincronizar | 0.312 | 0.089 |
| Persistencia | 0.373 | 0.046 |
| Persistencia 0/1 | 0.373 | 0.046 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
