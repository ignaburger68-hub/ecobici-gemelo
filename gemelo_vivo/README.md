# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 09:00 (hora de Ciudad de México).

## Último pronóstico: 24/11 09:00 a 10:00

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
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 11-15 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.97 | 8-13 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.97 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 0 / 10 | 0.96 | 0.04 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.95 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 0 / 11 | 0.95 | 0.03 | 0-7 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.94 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 113 (15/15) a 107-108 (1/56)
2. Llevar **17 bicis** de 115 (24/25) a 270 (1/27)
3. Llevar **11 bicis** de 118 (16/18) a 086 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

520 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.241 | 0.086 |
| Persistencia | 0.275 | 0.059 |
| Persistencia 0/1 | 0.275 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
