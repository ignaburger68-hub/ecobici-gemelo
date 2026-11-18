# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 10:42 (hora de Ciudad de México).

## Último pronóstico: 18/11 10:42 a 11:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.1 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 13 / 13 | 0.00 | 1.00 | 10-13 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 1.00 | 25-30 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 7-11 |
| 270 De la República-Ponciano Arr | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.99 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 30 | 0.97 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.96 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (30/30) a 107-108 (0/54)
2. Llevar **11 bicis** de 118 (13/13) a 270 (0/26)
3. Llevar **8 bicis** de 115 (19/21) a 086 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

101 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.026 |
| Sin resincronizar | 0.311 | 0.084 |
| Persistencia | 0.356 | 0.047 |
| Persistencia 0/1 | 0.356 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
