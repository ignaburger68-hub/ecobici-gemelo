# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 16:41 (hora de Ciudad de México).

## Último pronóstico: 20/11 16:41 a 17:41

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
| 116 Londres-Roma | 22 / 22 | 0.00 | 1.00 | 18-22 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 8-15 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.97 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.97 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 22 / 23 | 0.00 | 0.93 | 17-23 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.89 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 11 | 0.89 | 0.01 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 22 | 0.79 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 116 (22/22) a 010 (0/25)
2. Llevar **16 bicis** de 029 (30/33) a 003 (1/29)
3. Llevar **12 bicis** de 114 (22/23) a 112 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

268 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.034 |
| Sin resincronizar | 0.271 | 0.093 |
| Persistencia | 0.308 | 0.067 |
| Persistencia 0/1 | 0.308 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
