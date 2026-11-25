# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 11:22 (hora de Ciudad de México).

## Último pronóstico: 25/11 11:22 a 12:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 029 Reforma - Bucareli | 0 / 29 | 1.00 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 26 | 1.00 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 30 | 0.86 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.84 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 57 | 0.82 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.80 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 1 / 27 | 0.77 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 3 / 14 | 0.71 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 031 (32/34) a 029 (0/29)
2. Llevar **15 bicis** de 117 (23/28) a 270 (0/26)
3. Llevar **9 bicis** de 118 (15/17) a 555 (2/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

601 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.265 | 0.060 |
| Persistencia 0/1 | 0.265 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
