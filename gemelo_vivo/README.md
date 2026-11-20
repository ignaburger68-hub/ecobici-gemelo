# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 13:51 (hora de Ciudad de México).

## Último pronóstico: 20/11 13:51 a 14:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 1.00 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 33 | 0.99 | 0.00 | 0-9 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 16-22 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.98 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.91 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.87 | 0.01 | 0-8 |
| 010 Reforma - Ramírez | 1 / 25 | 0.86 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 14 / 15 | 0.00 | 0.86 | 7-15 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 116 (22/22) a 041 (0/29)
2. Llevar **17 bicis** de 031 (32/34) a 555 (0/33)
3. Llevar **8 bicis** de 113 (14/15) a 012 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

256 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.274 | 0.091 |
| Persistencia | 0.312 | 0.066 |
| Persistencia 0/1 | 0.312 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
