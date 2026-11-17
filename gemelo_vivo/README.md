# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 14:47 (hora de Ciudad de México).

## Último pronóstico: 17/11 14:47 a 15:47

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 9 | 0.99 | 0.01 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 9 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.98 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 9 | 0.97 | 0.01 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.96 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 16 | 0.94 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.94 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 117 (19/28) a 270 (0/25)
2. Llevar **6 bicis** de 113 (9/10) a 260 (1/18)
3. Llevar **7 bicis** de 098 (12/30) a 010 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

47 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.149 | 0.031 |
| Sin resincronizar | 0.229 | 0.095 |
| Persistencia | 0.303 | 0.059 |
| Persistencia 0/1 | 0.303 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
