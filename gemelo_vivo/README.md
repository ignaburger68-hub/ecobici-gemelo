# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 10:53 (hora de Ciudad de México).

## Último pronóstico: 25/11 10:53 a 11:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 12 / 12 | 0.00 | 0.98 | 7-12 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.97 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 0 / 11 | 0.93 | 0.03 | 2-8 |
| 107-108 Tolsa-Balderas | 1 / 57 | 0.93 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.87 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 33 / 34 | 0.00 | 0.85 | 29-34 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.76 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 031 (33/34) a 270 (0/26)
2. Llevar **7 bicis** de 026 (12/12) a 107-108 (1/57)
3. Llevar **11 bicis** de 115 (23/25) a 041 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

599 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
