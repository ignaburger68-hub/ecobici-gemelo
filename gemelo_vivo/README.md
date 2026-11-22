# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 20:14 (hora de Ciudad de México).

## Último pronóstico: 21/11 20:14 a 21:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.9 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 16 | 0.97 | 0.01 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.79 | 0.00 | 1-11 |
| 026 Reforma - Versalles | 1 / 14 | 0.73 | 0.01 | 0-8 |
| 010 Reforma - Ramírez | 2 / 27 | 0.57 | 0.00 | 0-8 |
| 048 Independencia - Azueta | 9 / 11 | 0.01 | 0.49 | 5-11 |
| 115 Roma-Dinamarca | 3 / 27 | 0.47 | 0.00 | 0-9 |
| 012 Río Lerma - Villalongín | 2 / 15 | 0.43 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.33 | 0.00 | 0-6 |
| 450 Ramos Arizpe- Av México Teno | 27 / 30 | 0.00 | 0.31 | 24-30 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (27/30) a 041 (1/32)
2. Llevar **6 bicis** de 048 (9/11) a 008 (0/16)
3. Llevar **8 bicis** de 259 (25/27) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

354 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
