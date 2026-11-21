# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 20:16 (hora de Ciudad de México).

## Último pronóstico: 20/11 20:16 a 21:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.2 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.98 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.00 | 1-8 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.87 | 15-19 |
| 048 Independencia - Azueta | 1 / 9 | 0.74 | 0.02 | 0-6 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.66 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 11 / 12 | 0.01 | 0.66 | 6-12 |
| 012 Río Lerma - Villalongín | 1 / 12 | 0.62 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 30 / 32 | 0.00 | 0.55 | 26-32 |
| 086 Sullivan-Insurgentes | 2 / 13 | 0.54 | 0.02 | 0-7 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (18/19) a 020 (0/21)
2. Llevar **7 bicis** de 029 (30/32) a 113 (0/15)
3. Llevar **5 bicis** de 026 (11/12) a 118 (1/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

283 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
