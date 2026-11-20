# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 11:25 (hora de Ciudad de México).

## Último pronóstico: 20/11 11:25 a 12:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 1.00 | 27-30 |
| 048 Independencia - Azueta | 10 / 10 | 0.00 | 0.99 | 6-10 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.99 | 11-15 |
| 555 Ribera de San Cosme - Insurg | 1 / 32 | 0.91 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.86 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.84 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.78 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.74 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.74 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 117 (30/30) a 555 (1/32)
2. Llevar **9 bicis** de 113 (15/15) a 255 (1/33)
3. Llevar **6 bicis** de 048 (10/10) a 012 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

246 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.279 | 0.091 |
| Persistencia | 0.317 | 0.064 |
| Persistencia 0/1 | 0.317 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
