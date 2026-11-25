# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 10:11 (hora de Ciudad de México).

## Último pronóstico: 25/11 10:11 a 11:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · lluvia 0.1 mm/h · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.92 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 0 / 12 | 0.92 | 0.01 | 2-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.87 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 11 / 12 | 0.00 | 0.83 | 7-12 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.69 | 0.00 | 0-7 |
| 107-108 Tolsa-Balderas | 3 / 57 | 0.62 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 28 / 31 | 0.00 | 0.57 | 22-31 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 026 (11/12) a 555 (1/30)
2. Llevar **12 bicis** de 029 (28/31) a 086 (0/17)
3. Llevar **11 bicis** de 115 (22/25) a 041 (0/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

596 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.238 | 0.081 |
| Persistencia | 0.266 | 0.060 |
| Persistencia 0/1 | 0.266 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
