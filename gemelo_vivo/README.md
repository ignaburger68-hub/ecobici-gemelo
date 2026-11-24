# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 18:05 (hora de Ciudad de México).

## Último pronóstico: 23/11 18:05 a 19:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.5 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.76** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 14-20 |
| 115 Roma-Dinamarca | 0 / 24 | 1.00 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 2 / 29 | 0.98 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 1 / 14 | 0.95 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.94 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 1 / 26 | 0.91 | 0.00 | 0-6 |
| 118 Liverpool-Dinamarca | 2 / 18 | 0.87 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 9 | 0.85 | 0.04 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (20/20) a 117 (2/29)
2. Llevar **17 bicis** de 029 (27/32) a 115 (0/24)
3. Llevar **8 bicis** de 555 (13/25) a 012 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

487 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.031 |
| Sin resincronizar | 0.253 | 0.087 |
| Persistencia | 0.288 | 0.059 |
| Persistencia 0/1 | 0.288 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
