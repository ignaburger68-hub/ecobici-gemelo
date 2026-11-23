# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 18:02 (hora de Ciudad de México).

## Último pronóstico: 22/11 18:02 a 19:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.3 °C** · lluvia 0.7 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.53** y las **devoluciones por 0.59** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.98 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 22 | 0.90 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 2 / 35 | 0.80 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 31 / 33 | 0.00 | 0.69 | 28-33 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.66 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 2 / 25 | 0.55 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 2 / 17 | 0.41 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 5 / 19 | 0.36 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 4 / 32 | 0.30 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 029 (31/33) a 031 (2/35)
2. Llevar **15 bicis** de 259 (22/25) a 114 (1/22)
3. Llevar **4 bicis** de 048 (8/11) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

416 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
