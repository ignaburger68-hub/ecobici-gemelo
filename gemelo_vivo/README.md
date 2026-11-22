# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 17:48 (hora de Ciudad de México).

## Último pronóstico: 22/11 17:48 a 18:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.3 °C** · lluvia 0.7 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.55** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 6-11 |
| 114 Lucerna-Abraham González | 0 / 22 | 0.98 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.71 | 0.00 | 0-5 |
| 031 Hamburgo - Insurgentes | 2 / 34 | 0.67 | 0.00 | 0-6 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.63 | 0.00 | 0-2 |
| 029 Reforma - Bucareli | 31 / 33 | 0.00 | 0.60 | 27-33 |
| 115 Roma-Dinamarca | 2 / 25 | 0.48 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 2 / 15 | 0.46 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 9 / 11 | 0.01 | 0.40 | 5-11 |
| 555 Ribera de San Cosme - Insurg | 4 / 31 | 0.35 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (31/33) a 114 (0/22)
2. Llevar **7 bicis** de 026 (11/11) a 031 (2/34)
3. Llevar **4 bicis** de 048 (9/11) a 086 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

415 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
