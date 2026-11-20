# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 08:49 (hora de Ciudad de México).

## Último pronóstico: 20/11 08:49 a 09:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 1 / 28 | 0.93 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 2 / 32 | 0.92 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 8 / 15 | 0.00 | 0.90 | 9-15 |
| 029 Reforma - Bucareli | 3 / 34 | 0.90 | 0.00 | 1-9 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.82 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.81 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 21 / 30 | 0.00 | 0.79 | 26-30 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.78 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (21/30) a 029 (3/34)
2. Llevar **8 bicis** de 113 (8/15) a 255 (2/32)
3. Llevar **5 bicis** de 114 (6/22) a 041 (1/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

235 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.286 | 0.093 |
| Persistencia | 0.324 | 0.063 |
| Persistencia 0/1 | 0.324 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
