# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 15:57 (hora de Ciudad de México).

## Último pronóstico: 23/11 15:57 a 16:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.73** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 11 | 0.85 | 0.01 | 0-5 |
| 118 Liverpool-Dinamarca | 1 / 18 | 0.81 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 2 / 14 | 0.45 | 0.01 | 1-8 |
| 041 Reforma - Av. de la Repúblic | 3 / 32 | 0.40 | 0.00 | 0-8 |
| 003 Reforma - Insurgentes | 3 / 27 | 0.39 | 0.00 | 0-8 |
| 555 Ribera de San Cosme - Insurg | 4 / 28 | 0.38 | 0.00 | 1-11 |
| 113 General Prim-Versalles | 3 / 14 | 0.35 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 3 / 19 | 0.33 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 029 (21/34) a 010 (0/25)
2. Llevar **10 bicis** de 031 (26/35) a 118 (1/18)
3. Llevar **5 bicis** de 116 (14/22) a 026 (1/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

478 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.290 | 0.061 |
| Persistencia 0/1 | 0.290 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
