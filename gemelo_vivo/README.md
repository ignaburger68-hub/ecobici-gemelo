# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 06:53 (hora de Ciudad de México).

## Último pronóstico: 22/11 06:52 a 07:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.4 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 116 Londres-Roma | 0 / 22 | 0.98 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.97 | 26-30 |
| 259 Tómas Alva Edison-Ponciano A | 26 / 27 | 0.00 | 0.53 | 24-27 |
| 086 Sullivan-Insurgentes | 2 / 14 | 0.45 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.40 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 17 | 0.35 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 1 / 27 | 0.29 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.27 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 15 | 0.24 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 31 | 0.18 | 0.00 | 1-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 450 (30/30) a 116 (0/22)
2. Llevar **5 bicis** de 259 (26/27) a 086 (2/14)
3. Llevar **9 bicis** de 270 (25/31) a 260 (2/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

369 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
