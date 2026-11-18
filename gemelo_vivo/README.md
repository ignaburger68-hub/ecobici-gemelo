# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 14:59 (hora de Ciudad de México).

## Último pronóstico: 18/11 14:59 a 15:59

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.1 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 107-108 Tolsa-Balderas | 0 / 52 | 0.99 | 0.00 | 1-9 |
| 114 Lucerna-Abraham González | 0 / 18 | 0.99 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 1 / 8 | 0.95 | 0.02 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 13 | 0.90 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 25 | 0.89 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.85 | 0.01 | 0-5 |
| 113 General Prim-Versalles | 1 / 10 | 0.83 | 0.02 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.83 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 11 | 0.74 | 0.05 | 0-8 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (28/30) a 010 (1/25)
2. Llevar **7 bicis** de 116 (15/17) a 107-108 (0/52)
3. Llevar **8 bicis** de 031 (25/32) a 118 (1/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

119 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.031 |
| Sin resincronizar | 0.304 | 0.083 |
| Persistencia | 0.341 | 0.060 |
| Persistencia 0/1 | 0.341 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
