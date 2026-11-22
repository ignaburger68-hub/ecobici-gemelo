# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 11:52 (hora de Ciudad de México).

## Último pronóstico: 22/11 11:52 a 12:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.1 mm/h · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.93** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 23 | 0.98 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.96 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.87 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 16 | 0.82 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 1 / 26 | 0.79 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 2 / 30 | 0.76 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (16/19) a 116 (0/23)
2. Llevar **15 bicis** de 259 (25/26) a 010 (3/27)
3. Llevar **6 bicis** de 048 (9/11) a 085 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

390 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
