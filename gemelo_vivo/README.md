# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 14:18 (hora de Ciudad de México).

## Último pronóstico: 23/11 14:18 a 15:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · lluvia 0.1 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 11 / 11 | 0.11 | 0.98 | 1-10 |
| 010 Reforma - Ramírez | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 0.98 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.96 | 0.01 | 0-7 |
| 107-108 Tolsa-Balderas | 1 / 56 | 0.90 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.83 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 2 / 20 | 0.83 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 2 / 14 | 0.77 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 3 / 16 | 0.70 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 117 (26/30) a 010 (0/26)
2. Llevar **5 bicis** de 048 (11/11) a 107-108 (1/56)
3. Llevar **8 bicis** de 116 (14/22) a 020 (2/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

471 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.032 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.062 |
| Persistencia 0/1 | 0.291 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
