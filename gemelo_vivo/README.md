# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 15:30 (hora de Ciudad de México).

## Último pronóstico: 17/11 15:30 a 16:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.8 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 026 Reforma - Versalles | 0 / 9 | 1.00 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.98 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 0 / 9 | 0.97 | 0.03 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.97 | 0.09 | 0-7 |
| 115 Roma-Dinamarca | 1 / 24 | 0.95 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.92 | 0.00 | 1-8 |
| 270 De la República-Ponciano Arr | 1 / 24 | 0.92 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.86 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 098 (14/30) a 010 (1/27)
2. Llevar **8 bicis** de 117 (22/30) a 259 (0/24)
3. Llevar **5 bicis** de 117 (22/30) a 115 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

50 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.151 | 0.030 |
| Sin resincronizar | 0.239 | 0.094 |
| Persistencia | 0.317 | 0.056 |
| Persistencia 0/1 | 0.317 | 0.056 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
