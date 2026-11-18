# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 20:16 (hora de Ciudad de México).

## Último pronóstico: 17/11 20:15 a 21:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.9 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 0 / 24 | 1.00 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.99 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 9 | 0.99 | 0.01 | 0-4 |
| 048 Independencia - Azueta | 0 / 9 | 0.99 | 0.01 | 0-5 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.98 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 1 / 31 | 0.97 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 450 (25/26) a 003 (1/31)
2. Llevar **11 bicis** de 260 (16/18) a 041 (0/20)
3. Llevar **11 bicis** de 555 (29/29) a 115 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

70 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.135 | 0.027 |
| Sin resincronizar | 0.316 | 0.090 |
| Persistencia | 0.372 | 0.047 |
| Persistencia 0/1 | 0.372 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
