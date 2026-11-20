# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 16:56 (hora de Ciudad de México).

## Último pronóstico: 20/11 16:56 a 17:56

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 23 / 23 | 0.00 | 0.99 | 17-23 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 18-22 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 9-15 |
| 008 Reforma - General Prim | 13 / 14 | 0.01 | 0.97 | 7-14 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.96 | 0.00 | 0-8 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.92 | 26-33 |
| 048 Independencia - Azueta | 7 / 8 | 0.03 | 0.92 | 4-8 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.88 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (16/20) a 010 (0/25)
2. Llevar **15 bicis** de 116 (22/22) a 003 (1/29)
3. Llevar **13 bicis** de 029 (32/33) a 020 (1/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

269 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.271 | 0.093 |
| Persistencia | 0.308 | 0.066 |
| Persistencia 0/1 | 0.308 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
