# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 10:54 (hora de Ciudad de México).

## Último pronóstico: 22/11 10:54 a 11:54

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
| 112 Av. Morelos-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.94 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 1 / 33 | 0.94 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.92 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 17 | 0.91 | 0.00 | 0-4 |
| 116 Londres-Roma | 2 / 23 | 0.91 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 1 / 14 | 0.90 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 3 / 29 | 0.90 | 0.00 | 0-7 |
| 115 Roma-Dinamarca | 1 / 25 | 0.90 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 259 (24/26) a 041 (3/29)
2. Llevar **14 bicis** de 107-108 (23/59) a 020 (1/21)
3. Llevar **10 bicis** de 270 (19/30) a 029 (1/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

386 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
