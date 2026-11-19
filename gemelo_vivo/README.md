# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 06:10 (hora de Ciudad de México).

## Último pronóstico: 19/11 06:09 a 07:09

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.8 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 9 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 25 / 25 | 0.00 | 0.98 | 20-25 |
| 119 Turín-Abraham González | 0 / 5 | 0.97 | 0.09 | 0-4 |
| 260 Av. Juárez-Balderas | 17 / 17 | 0.00 | 0.96 | 10-17 |
| 256 Gómez Farías-Sadi Carnot | 1 / 18 | 0.89 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 18 | 0.80 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 1 / 11 | 0.74 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.36 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 010 (9/27) a 256 (1/18)
2. Llevar **6 bicis** de 260 (17/17) a 048 (0/9)
3. Llevar **10 bicis** de 450 (25/25) a 114 (1/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

156 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.035 |
| Sin resincronizar | 0.291 | 0.093 |
| Persistencia | 0.334 | 0.069 |
| Persistencia 0/1 | 0.334 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
