# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 17:10 (hora de Ciudad de México).

## Último pronóstico: 20/11 17:10 a 18:10

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
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 19-22 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 0 / 28 | 0.98 | 0.00 | 0-9 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.97 | 29-33 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.97 | 0.00 | 1-7 |
| 086 Sullivan-Insurgentes | 0 / 13 | 0.97 | 0.17 | 2-13 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.97 | 15-20 |
| 113 General Prim-Versalles | 15 / 15 | 0.01 | 0.97 | 8-15 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.96 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 029 (33/33) a 010 (0/25)
2. Llevar **14 bicis** de 260 (19/20) a 003 (0/28)
3. Llevar **14 bicis** de 116 (22/22) a 112 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

270 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
