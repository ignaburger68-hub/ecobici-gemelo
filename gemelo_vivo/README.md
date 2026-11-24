# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 11:52 (hora de Ciudad de México).

## Último pronóstico: 24/11 11:52 a 12:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · lluvia 0.5 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.89** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 32 | 0.99 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.98 | 12-18 |
| 085 Rosas Moreno - Sullivan | 0 / 10 | 0.98 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.76 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 2 / 28 | 0.63 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.61 | 0.00 | 1-8 |
| 113 General Prim-Versalles | 13 / 15 | 0.00 | 0.58 | 9-15 |
| 026 Reforma - Versalles | 12 / 13 | 0.00 | 0.57 | 6-13 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 118 (19/19) a 041 (0/32)
2. Llevar **7 bicis** de 113 (13/15) a 112 (0/20)
3. Llevar **5 bicis** de 114 (18/22) a 085 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

532 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.242 | 0.085 |
| Persistencia | 0.275 | 0.061 |
| Persistencia 0/1 | 0.275 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
