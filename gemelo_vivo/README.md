# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 14:16 (hora de Ciudad de México).

## Último pronóstico: 21/11 14:16 a 15:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.97** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 10 / 10 | 0.03 | 0.98 | 4-10 |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.97 | 24-30 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.84 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.80 | 13-20 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.74 | 0.00 | 0-8 |
| 010 Reforma - Ramírez | 2 / 27 | 0.70 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.68 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.67 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 28 / 30 | 0.00 | 0.66 | 22-30 |
| 555 Ribera de San Cosme - Insurg | 33 / 35 | 0.00 | 0.62 | 24-34 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 450 (30/30) a 041 (1/31)
2. Llevar **14 bicis** de 270 (28/30) a 010 (2/27)
3. Llevar **5 bicis** de 048 (10/10) a 086 (1/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

329 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
