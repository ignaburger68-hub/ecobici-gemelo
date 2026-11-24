# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 08:18 (hora de Ciudad de México).

## Último pronóstico: 24/11 08:18 a 09:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.7 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 14-15 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.98 | 0.00 | 1-8 |
| 107-108 Tolsa-Balderas | 4 / 56 | 0.92 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.92 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.91 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 4 / 14 | 0.87 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 3 / 21 | 0.85 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 2 / 29 | 0.83 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 6 / 27 | 0.80 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 3 / 20 | 0.79 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 113 (15/15) a 555 (0/31)
2. Llevar **17 bicis** de 115 (19/26) a 107-108 (4/56)
3. Llevar **13 bicis** de 117 (14/29) a 041 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

517 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.242 | 0.087 |
| Persistencia | 0.275 | 0.059 |
| Persistencia 0/1 | 0.275 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
