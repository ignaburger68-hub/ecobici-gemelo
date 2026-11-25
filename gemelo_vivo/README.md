# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 12:33 (hora de Ciudad de México).

## Último pronóstico: 25/11 12:33 a 13:33

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
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.96 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.92 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.84 | 0.00 | 0-3 |
| 117 Londres-Nápoles | 27 / 28 | 0.00 | 0.82 | 21-27 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.77 | 0.01 | 0-7 |
| 450 Ramos Arizpe- Av México Teno | 1 / 27 | 0.77 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (27/28) a 555 (1/30)
2. Llevar **11 bicis** de 115 (23/24) a 041 (0/30)
3. Llevar **14 bicis** de 031 (27/33) a 270 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

606 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
