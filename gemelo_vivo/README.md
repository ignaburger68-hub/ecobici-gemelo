# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 17:38 (hora de Ciudad de México).

## Último pronóstico: 20/11 17:38 a 18:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.2 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.99 | 18-20 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.98 | 13-22 |
| 256 Gómez Farías-Sadi Carnot | 0 / 21 | 0.96 | 0.00 | 0-7 |
| 029 Reforma - Bucareli | 31 / 33 | 0.00 | 0.94 | 24-33 |
| 008 Reforma - General Prim | 3 / 15 | 0.86 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 2 / 21 | 0.84 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 1 / 28 | 0.65 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 2 / 29 | 0.52 | 0.00 | 0-10 |
| 026 Reforma - Versalles | 5 / 10 | 0.49 | 0.08 | 0-7 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 260 (20/20) a 020 (2/21)
2. Llevar **11 bicis** de 029 (31/33) a 008 (3/15)
3. Llevar **10 bicis** de 116 (22/22) a 256 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

272 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.271 | 0.093 |
| Persistencia | 0.308 | 0.067 |
| Persistencia 0/1 | 0.308 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
