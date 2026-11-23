# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 08:14 (hora de Ciudad de México).

## Último pronóstico: 23/11 08:14 a 09:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 0 / 18 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 12 | 1.00 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 0 / 27 | 0.98 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 4 / 56 | 0.98 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 0 / 16 | 0.97 | 0.00 | 1-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 32 | 0.96 | 0.00 | 0-2 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 115 (14/25) a 107-108 (4/56)
2. Llevar **8 bicis** de 113 (9/15) a 256 (0/21)
3. Llevar **10 bicis** de 117 (11/30) a 086 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

446 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.256 | 0.090 |
| Persistencia | 0.293 | 0.065 |
| Persistencia 0/1 | 0.293 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
