# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 20:30 (hora de Ciudad de México).

## Último pronóstico: 20/11 20:30 a 21:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 031 Hamburgo - Insurgentes | 34 / 34 | 0.00 | 0.99 | 29-34 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.01 | 0-7 |
| 029 Reforma - Bucareli | 30 / 32 | 0.00 | 0.85 | 27-32 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.83 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 17 / 19 | 0.00 | 0.74 | 13-19 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.73 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.72 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.68 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 11 / 14 | 0.01 | 0.51 | 7-13 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 031 (34/34) a 086 (1/15)
2. Llevar **13 bicis** de 029 (30/32) a 020 (1/21)
3. Llevar **7 bicis** de 260 (17/19) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

284 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.266 | 0.093 |
| Persistencia | 0.305 | 0.067 |
| Persistencia 0/1 | 0.305 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
