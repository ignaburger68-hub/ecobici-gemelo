# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 17:36 (hora de Ciudad de México).

## Último pronóstico: 23/11 17:36 a 18:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.5 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.70** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 115 Roma-Dinamarca | 1 / 24 | 0.98 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.95 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 26 | 0.93 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.90 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 18 | 0.90 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 1 / 14 | 0.90 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 19 | 0.79 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.78 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (16/20) a 117 (0/27)
2. Llevar **15 bicis** de 029 (20/32) a 115 (1/24)
3. Llevar **8 bicis** de 555 (12/26) a 010 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

485 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.288 | 0.059 |
| Persistencia 0/1 | 0.288 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
