# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 10:40 (hora de Ciudad de México).

## Último pronóstico: 22/11 10:40 a 11:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-8 |
| 048 Independencia - Azueta | 0 / 11 | 0.98 | 0.01 | 0-5 |
| 115 Roma-Dinamarca | 0 / 25 | 0.98 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 20 | 0.94 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.92 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.90 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 1 / 31 | 0.87 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 259 (25/26) a 041 (0/30)
2. Llevar **14 bicis** de 107-108 (23/59) a 010 (0/27)
3. Llevar **10 bicis** de 555 (21/33) a 020 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

385 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
