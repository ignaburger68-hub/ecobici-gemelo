# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 14:02 (hora de Ciudad de México).

## Último pronóstico: 21/11 14:02 a 15:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.99 | 25-30 |
| 048 Independencia - Azueta | 10 / 10 | 0.02 | 0.99 | 4-10 |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.97 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.96 | 0.00 | 0-8 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.84 | 14-20 |
| 555 Ribera de San Cosme - Insurg | 34 / 35 | 0.00 | 0.79 | 26-35 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.73 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 29 / 31 | 0.00 | 0.73 | 24-31 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.65 | 0.01 | 0-8 |
| 010 Reforma - Ramírez | 2 / 27 | 0.62 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (30/30) a 041 (0/31)
2. Llevar **6 bicis** de 048 (10/10) a 012 (0/15)
3. Llevar **13 bicis** de 270 (29/31) a 010 (2/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

328 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
