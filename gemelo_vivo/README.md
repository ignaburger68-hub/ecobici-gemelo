# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 17:22 (hora de Ciudad de México).

## Último pronóstico: 23/11 17:22 a 18:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-1 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.98 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.89 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 11 | 0.89 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.89 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.89 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (12/19) a 115 (0/24)
2. Llevar **7 bicis** de 086 (10/13) a 010 (0/26)
3. Llevar **10 bicis** de 029 (18/31) a 113 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

484 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.288 | 0.060 |
| Persistencia 0/1 | 0.288 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
