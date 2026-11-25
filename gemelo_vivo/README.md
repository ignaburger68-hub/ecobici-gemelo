# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 10:25 (hora de Ciudad de México).

## Último pronóstico: 25/11 10:25 a 11:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · lluvia 0.1 mm/h · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.79** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 12 / 12 | 0.00 | 1.00 | 8-12 |
| 098 Emilio Dondé-Av. Balderas | 0 / 11 | 0.91 | 0.02 | 1-8 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.88 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.86 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.82 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.81 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.74 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 3 / 57 | 0.72 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.69 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 026 (12/12) a 555 (1/30)
2. Llevar **13 bicis** de 115 (23/25) a 107-108 (3/57)
3. Llevar **10 bicis** de 029 (29/31) a 086 (1/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

597 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
