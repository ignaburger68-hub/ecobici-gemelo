# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 17:24 (hora de Ciudad de México).

## Último pronóstico: 20/11 17:24 a 18:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 1.00 | 14-20 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 13-21 |
| 010 Reforma - Ramírez | 1 / 25 | 0.97 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.94 | 0.00 | 0-9 |
| 029 Reforma - Bucareli | 31 / 33 | 0.00 | 0.85 | 26-33 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.83 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 2 / 11 | 0.81 | 0.01 | 0-5 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.79 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 14 / 15 | 0.02 | 0.61 | 4-13 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 260 (20/20) a 010 (1/25)
2. Llevar **13 bicis** de 029 (31/33) a 020 (2/21)
3. Llevar **12 bicis** de 116 (22/22) a 003 (1/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

271 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.271 | 0.093 |
| Persistencia | 0.308 | 0.067 |
| Persistencia 0/1 | 0.308 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
