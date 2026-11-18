# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 09:17 (hora de Ciudad de México).

## Último pronóstico: 18/11 09:17 a 10:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-2 |
| 107-108 Tolsa-Balderas | 0 / 55 | 0.99 | 0.00 | 5-18 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 117 Londres-Nápoles | 29 / 31 | 0.00 | 0.98 | 16-29 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.97 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.97 | 0.00 | 5-19 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.97 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 11 / 11 | 0.01 | 0.96 | 8-11 |
| 026 Reforma - Versalles | 11 / 11 | 0.01 | 0.95 | 5-11 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.94 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (29/31) a 107-108 (0/55)
2. Llevar **11 bicis** de 115 (20/22) a 270 (1/26)
3. Llevar **6 bicis** de 113 (11/11) a 086 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

95 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.025 |
| Sin resincronizar | 0.316 | 0.086 |
| Persistencia | 0.359 | 0.044 |
| Persistencia 0/1 | 0.359 | 0.044 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
