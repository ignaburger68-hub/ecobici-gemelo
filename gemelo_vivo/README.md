# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 12:07 (hora de Ciudad de México).

## Último pronóstico: 18/11 12:07 a 13:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.96 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.96 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.96 | 11-19 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.91 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 1 / 9 | 0.82 | 0.00 | 0-4 |
| 107-108 Tolsa-Balderas | 1 / 54 | 0.79 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.79 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 2 / 31 | 0.75 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.73 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 115 (21/21) a 041 (0/24)
2. Llevar **13 bicis** de 117 (27/30) a 256 (1/19)
3. Llevar **14 bicis** de 031 (31/33) a 270 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

107 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.027 |
| Sin resincronizar | 0.307 | 0.083 |
| Persistencia | 0.350 | 0.052 |
| Persistencia 0/1 | 0.350 | 0.052 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
