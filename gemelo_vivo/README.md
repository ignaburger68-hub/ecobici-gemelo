# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 12:47 (hora de Ciudad de México).

## Último pronóstico: 25/11 12:47 a 13:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 0 / 30 | 1.00 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 25 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.97 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.97 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.94 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 30 | 0.87 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 12 | 0.86 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 116 (21/23) a 010 (0/25)
2. Llevar **15 bicis** de 117 (25/27) a 555 (0/30)
3. Llevar **14 bicis** de 098 (21/31) a 270 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

607 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.239 | 0.081 |
| Persistencia | 0.264 | 0.060 |
| Persistencia 0/1 | 0.264 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
