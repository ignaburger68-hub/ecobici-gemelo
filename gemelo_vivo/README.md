# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 17:05 (hora de Ciudad de México).

## Último pronóstico: 22/11 17:05 a 18:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.61** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 27 / 27 | 0.00 | 0.97 | 20-27 |
| 113 General Prim-Versalles | 1 / 15 | 0.78 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 25 | 0.76 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.76 | 22-26 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.70 | 6-11 |
| 114 Lucerna-Abraham González | 1 / 22 | 0.67 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 2 / 35 | 0.66 | 0.00 | 0-8 |
| 555 Ribera de San Cosme - Insurg | 3 / 32 | 0.56 | 0.00 | 0-7 |
| 256 Gómez Farías-Sadi Carnot | 3 / 22 | 0.53 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 4 / 31 | 0.52 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 041 (27/27) a 031 (2/35)
2. Llevar **14 bicis** de 259 (25/26) a 555 (3/32)
3. Llevar **5 bicis** de 026 (10/11) a 115 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

412 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
