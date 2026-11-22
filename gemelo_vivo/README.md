# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 17:20 (hora de Ciudad de México).

## Último pronóstico: 22/11 17:20 a 18:20

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.59** y las **devoluciones por 0.64** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 22 | 0.97 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.76 | 22-26 |
| 113 General Prim-Versalles | 1 / 15 | 0.74 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 2 / 32 | 0.72 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.72 | 26-33 |
| 256 Gómez Farías-Sadi Carnot | 2 / 22 | 0.69 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.67 | 6-11 |
| 041 Reforma - Av. de la Repúblic | 26 / 27 | 0.00 | 0.64 | 19-27 |
| 450 Ramos Arizpe- Av México Teno | 3 / 31 | 0.63 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 029 (32/33) a 555 (2/32)
2. Llevar **11 bicis** de 259 (25/26) a 114 (0/22)
3. Llevar **11 bicis** de 041 (26/27) a 450 (3/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

413 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
