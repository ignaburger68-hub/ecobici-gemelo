# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 10:16 (hora de Ciudad de México).

## Último pronóstico: 23/11 10:16 a 11:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 0 / 16 | 0.97 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 17 | 0.96 | 0.00 | 1-7 |
| 119 Turín-Abraham González | 0 / 28 | 0.96 | 0.00 | 0-7 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.95 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 0.93 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.69 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 2 / 11 | 0.68 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.66 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (15/19) a 107-108 (1/56)
2. Llevar **17 bicis** de 117 (24/30) a 555 (1/30)
3. Llevar **9 bicis** de 115 (21/24) a 086 (0/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

454 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.256 | 0.088 |
| Persistencia | 0.295 | 0.064 |
| Persistencia 0/1 | 0.295 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
