# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 15:43 (hora de Ciudad de México).

## Último pronóstico: 23/11 15:43 a 16:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · lluvia 0.2 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.83** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 11 | 0.97 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.92 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.90 | 0.00 | 1-9 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.79 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.76 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 2 / 11 | 0.68 | 0.01 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 3 / 32 | 0.62 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (21/35) a 010 (0/24)
2. Llevar **10 bicis** de 029 (19/34) a 260 (2/20)
3. Llevar **8 bicis** de 117 (20/29) a 026 (1/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

477 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
