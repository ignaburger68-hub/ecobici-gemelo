# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 14:19 (hora de Ciudad de México).

## Último pronóstico: 17/11 14:19 a 15:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 1.00 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 17 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.98 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.94 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 19 | 0.94 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.92 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 17 | 0.91 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 31 | 0.85 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 117 (21/30) a 118 (1/16)
2. Llevar **6 bicis** de 117 (21/30) a 041 (0/20)
3. Llevar **5 bicis** de 116 (8/17) a 256 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

45 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.149 | 0.030 |
| Sin resincronizar | 0.221 | 0.096 |
| Persistencia | 0.297 | 0.061 |
| Persistencia 0/1 | 0.297 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
