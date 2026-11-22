# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 16:36 (hora de Ciudad de México).

## Último pronóstico: 22/11 16:36 a 17:36

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
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.99 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 0 / 25 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.63 | 6-11 |
| 259 Tómas Alva Edison-Ponciano A | 23 / 25 | 0.00 | 0.46 | 20-25 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.40 | 0.00 | 0-9 |
| 086 Sullivan-Insurgentes | 3 / 12 | 0.36 | 0.03 | 0-8 |
| 008 Reforma - General Prim | 2 / 17 | 0.35 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 3 / 27 | 0.28 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 259 (23/25) a 555 (0/31)
2. Llevar **5 bicis** de 026 (10/11) a 113 (0/14)
3. Llevar **11 bicis** de 041 (24/27) a 115 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

410 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
