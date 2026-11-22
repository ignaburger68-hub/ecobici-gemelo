# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 19:30 (hora de Ciudad de México).

## Último pronóstico: 21/11 19:30 a 20:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.98 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 0 / 16 | 0.98 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 0 / 15 | 0.96 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.96 | 0.00 | 0-10 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.84 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 1 / 15 | 0.79 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.76 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.63 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 27 | 0.59 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (27/34) a 041 (0/32)
2. Llevar **16 bicis** de 450 (27/29) a 003 (0/28)
3. Llevar **15 bicis** de 555 (30/35) a 010 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

351 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
