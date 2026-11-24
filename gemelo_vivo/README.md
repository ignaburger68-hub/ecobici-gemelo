# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 13:03 (hora de Ciudad de México).

## Último pronóstico: 24/11 13:03 a 14:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.2 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.75** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 27 | 1.00 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 22 | 0.99 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 12-15 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.98 | 8-13 |
| 119 Turín-Abraham González | 0 / 25 | 0.98 | 0.00 | 0-7 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.95 | 0.02 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.90 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 3 / 20 | 0.73 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 1 / 26 | 0.69 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 10 | 0.69 | 0.01 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 113 (15/15) a 270 (0/27)
2. Llevar **8 bicis** de 026 (13/13) a 041 (1/32)
3. Llevar **14 bicis** de 031 (32/35) a 119 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

537 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.113 | 0.032 |
| Sin resincronizar | 0.241 | 0.085 |
| Persistencia | 0.272 | 0.061 |
| Persistencia 0/1 | 0.272 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
