# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 17:34 (hora de Ciudad de México).

## Último pronóstico: 22/11 17:34 a 18:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.3 °C** · lluvia 0.7 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.57** y las **devoluciones por 0.63** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.98 | 7-11 |
| 114 Lucerna-Abraham González | 1 / 22 | 0.72 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 1 / 15 | 0.72 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.69 | 27-33 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.68 | 22-26 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.57 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 2 / 25 | 0.54 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.53 | 0.00 | 0-7 |
| 450 Ramos Arizpe- Av México Teno | 3 / 31 | 0.48 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (32/33) a 031 (3/35)
2. Llevar **6 bicis** de 026 (11/11) a 114 (1/22)
3. Llevar **7 bicis** de 259 (25/26) a 113 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

414 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
