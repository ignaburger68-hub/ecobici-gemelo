# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 09:03 (hora de Ciudad de México).

## Último pronóstico: 20/11 09:03 a 10:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 13 / 15 | 0.00 | 1.00 | 10-15 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 17 | 0.99 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 28 / 30 | 0.00 | 0.98 | 21-29 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.92 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.88 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.85 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.77 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.69 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (28/30) a 086 (0/17)
2. Llevar **13 bicis** de 113 (13/15) a 255 (2/33)
3. Llevar **9 bicis** de 117 (28/30) a 256 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

236 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.120 | 0.034 |
| Sin resincronizar | 0.285 | 0.092 |
| Persistencia | 0.324 | 0.063 |
| Persistencia 0/1 | 0.324 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
