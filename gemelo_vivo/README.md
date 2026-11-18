# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 07:07 (hora de Ciudad de México).

## Último pronóstico: 18/11 07:07 a 08:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 1 / 18 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 4 | 0.99 | 0.31 | 0-3 |
| 048 Independencia - Azueta | 0 / 7 | 0.99 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 0.98 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.97 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.01 | 0.92 | 11-23 |
| 031 Hamburgo - Insurgentes | 2 / 24 | 0.85 | 0.00 | 1-8 |
| 026 Reforma - Versalles | 5 / 9 | 0.01 | 0.73 | 6-9 |
| 020 Reforma- Río Támesis | 1 / 8 | 0.66 | 0.27 | 1-8 |
| 256 Gómez Farías-Sadi Carnot | 4 / 19 | 0.61 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 450 (27/27) a 260 (1/18)
2. Llevar **7 bicis** de 118 (7/15) a 031 (2/24)
3. Llevar **4 bicis** de 026 (5/9) a 119 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

86 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.320 | 0.092 |
| Persistencia | 0.351 | 0.045 |
| Persistencia 0/1 | 0.351 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
