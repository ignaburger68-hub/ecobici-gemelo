# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 18:34 (hora de Ciudad de México).

## Último pronóstico: 21/11 18:33 a 19:33

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-9 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 15 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.98 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 0 / 27 | 0.97 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 1 / 23 | 0.88 | 0.00 | 0-7 |
| 112 Av. Morelos-Abraham González | 2 / 22 | 0.88 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 1 / 15 | 0.85 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 26 | 0.65 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 3 / 32 | 0.59 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 259 (23/25) a 041 (0/31)
2. Llevar **8 bicis** de 260 (17/19) a 086 (0/15)
3. Llevar **13 bicis** de 450 (23/30) a 115 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

347 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
