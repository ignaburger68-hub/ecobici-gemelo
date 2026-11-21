# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 20:02 (hora de Ciudad de México).

## Último pronóstico: 20/11 20:02 a 21:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.2 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 0 / 17 | 1.00 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.98 | 16-19 |
| 113 General Prim-Versalles | 1 / 15 | 0.78 | 0.00 | 1-8 |
| 012 Río Lerma - Villalongín | 1 / 13 | 0.77 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 32 / 34 | 0.00 | 0.72 | 25-33 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.69 | 25-33 |
| 048 Independencia - Azueta | 1 / 9 | 0.65 | 0.03 | 0-5 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.60 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 4 / 28 | 0.55 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (19/19) a 118 (0/17)
2. Llevar **14 bicis** de 555 (32/34) a 003 (4/28)
3. Llevar **7 bicis** de 031 (32/33) a 113 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

282 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
