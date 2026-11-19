# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 15:12 (hora de Ciudad de México).

## Último pronóstico: 19/11 15:12 a 16:12

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 0 / 10 | 1.00 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 13 | 1.00 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 0 / 23 | 0.99 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 21 | 0.99 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 116 (16/16) a 010 (0/27)
2. Llevar **9 bicis** de 114 (13/17) a 260 (0/20)
3. Llevar **10 bicis** de 117 (17/26) a 115 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

191 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.037 |
| Sin resincronizar | 0.287 | 0.094 |
| Persistencia | 0.331 | 0.071 |
| Persistencia 0/1 | 0.331 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
