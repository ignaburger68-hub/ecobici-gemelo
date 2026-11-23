# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 16:40 (hora de Ciudad de México).

## Último pronóstico: 23/11 16:40 a 17:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.70** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.98 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.83 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 2 / 13 | 0.52 | 0.03 | 0-9 |
| 012 Río Lerma - Villalongín | 3 / 13 | 0.40 | 0.01 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 4 / 26 | 0.40 | 0.00 | 2-13 |
| 112 Av. Morelos-Abraham González | 4 / 19 | 0.29 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (29/35) a 010 (0/26)
2. Llevar **11 bicis** de 029 (20/34) a 003 (0/26)
3. Llevar **6 bicis** de 116 (10/22) a 026 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

481 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.290 | 0.060 |
| Persistencia 0/1 | 0.290 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
