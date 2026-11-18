# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 07:21 (hora de Ciudad de México).

## Último pronóstico: 18/11 07:21 a 08:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 7 | 0.99 | 0.01 | 0-3 |
| 260 Av. Juárez-Balderas | 3 / 18 | 0.98 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 0 / 7 | 0.92 | 0.40 | 0-7 |
| 086 Sullivan-Insurgentes | 2 / 5 | 0.91 | 0.29 | 0-3 |
| 119 Turín-Abraham González | 1 / 25 | 0.87 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 3 / 18 | 0.74 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 4 / 9 | 0.01 | 0.70 | 5-9 |
| 118 Liverpool-Dinamarca | 10 / 15 | 0.00 | 0.67 | 9-15 |
| 270 De la República-Ponciano Arr | 4 / 21 | 0.55 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 118 (10/15) a 260 (3/18)
2. Llevar **4 bicis** de 026 (4/9) a 119 (1/25)
3. Llevar **10 bicis** de 029 (17/31) a 256 (3/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

87 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.318 | 0.091 |
| Persistencia | 0.349 | 0.045 |
| Persistencia 0/1 | 0.349 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
