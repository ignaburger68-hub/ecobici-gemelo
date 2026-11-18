# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 14:45 (hora de Ciudad de México).

## Último pronóstico: 18/11 14:45 a 15:45

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
| 114 Lucerna-Abraham González | 0 / 18 | 0.99 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.01 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 10 | 0.98 | 0.09 | 0-8 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 0.97 | 22-30 |
| 048 Independencia - Azueta | 1 / 7 | 0.95 | 0.03 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.91 | 0.00 | 0-5 |
| 107-108 Tolsa-Balderas | 1 / 52 | 0.90 | 0.00 | 1-9 |
| 118 Liverpool-Dinamarca | 1 / 13 | 0.89 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.84 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.81 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (30/30) a 270 (1/26)
2. Llevar **8 bicis** de 031 (32/33) a 118 (1/13)
3. Llevar **10 bicis** de 031 (32/33) a 114 (0/18)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

118 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.031 |
| Sin resincronizar | 0.305 | 0.083 |
| Persistencia | 0.341 | 0.060 |
| Persistencia 0/1 | 0.341 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
