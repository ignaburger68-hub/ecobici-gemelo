# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 07:35 (hora de Ciudad de México).

## Último pronóstico: 19/11 07:35 a 08:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.8 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 18 | 1.00 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 23 | 0.97 | 0.00 | 0-1 |
| 256 Gómez Farías-Sadi Carnot | 1 / 18 | 0.97 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.97 | 0.00 | 0-9 |
| 118 Liverpool-Dinamarca | 13 / 13 | 0.00 | 0.97 | 8-13 |
| 086 Sullivan-Insurgentes | 3 / 11 | 0.94 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 9 | 0.86 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 8 / 16 | 0.84 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (13/13) a 259 (2/23)
2. Llevar **10 bicis** de 029 (13/35) a 256 (1/18)
3. Llevar **6 bicis** de 026 (7/15) a 041 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

159 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.286 | 0.091 |
| Persistencia | 0.332 | 0.068 |
| Persistencia 0/1 | 0.332 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
