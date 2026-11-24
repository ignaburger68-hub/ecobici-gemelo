# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 08:32 (hora de Ciudad de México).

## Último pronóstico: 24/11 08:32 a 09:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 12-15 |
| 086 Sullivan-Insurgentes | 0 / 15 | 1.00 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 55 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 2 / 29 | 0.98 | 0.00 | 0-7 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.96 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 1 / 21 | 0.96 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.90 | 0.03 | 1-7 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.84 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 32 | 0.71 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 3 / 29 | 0.69 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 113 (15/15) a 107-108 (1/55)
2. Llevar **15 bicis** de 115 (19/26) a 555 (2/29)
3. Llevar **12 bicis** de 117 (17/30) a 086 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

518 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.087 |
| Persistencia | 0.275 | 0.059 |
| Persistencia 0/1 | 0.275 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
