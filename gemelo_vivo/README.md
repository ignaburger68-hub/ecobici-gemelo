# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 16:26 (hora de Ciudad de México).

## Último pronóstico: 23/11 16:26 a 17:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.69** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.98 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 11 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 13 | 0.76 | 0.02 | 0-7 |
| 555 Ribera de San Cosme - Insurg | 2 / 26 | 0.74 | 0.00 | 0-8 |
| 112 Av. Morelos-Abraham González | 2 / 18 | 0.38 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 2 / 11 | 0.30 | 0.03 | 1-8 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 029 (19/34) a 010 (0/26)
2. Llevar **9 bicis** de 031 (28/35) a 118 (0/18)
3. Llevar **8 bicis** de 031 (28/35) a 003 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

480 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
