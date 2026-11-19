# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 08:03 (hora de Ciudad de México).

## Último pronóstico: 19/11 08:03 a 09:03

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
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 255 José Rosas Moreno-Guillermo  | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 1 / 26 | 1.00 | 0.00 | 0-1 |
| 260 Av. Juárez-Balderas | 0 / 16 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 23 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 1 / 11 | 1.00 | 0.00 | 0-2 |
| 270 De la República-Ponciano Arr | 3 / 25 | 1.00 | 0.00 | 0-1 |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 117 (10/29) a 555 (1/26)
2. Llevar **10 bicis** de 026 (10/15) a 259 (2/23)
3. Llevar **11 bicis** de 115 (11/23) a 270 (3/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

161 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.035 |
| Sin resincronizar | 0.284 | 0.090 |
| Persistencia | 0.333 | 0.068 |
| Persistencia 0/1 | 0.333 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
