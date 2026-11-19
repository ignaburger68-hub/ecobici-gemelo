# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 10:25 (hora de Ciudad de México).

## Último pronóstico: 19/11 10:25 a 11:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.0 °C** · sin lluvia · viento 2 km/h · día hábil

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
| 107-108 Tolsa-Balderas | 0 / 57 | 1.00 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 13 / 13 | 0.00 | 0.99 | 8-13 |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.98 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.98 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 13 / 14 | 0.00 | 0.90 | 10-14 |
| 115 Roma-Dinamarca | 21 / 23 | 0.00 | 0.86 | 20-23 |
| 116 Londres-Roma | 18 / 18 | 0.00 | 0.85 | 9-18 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 117 (26/28) a 107-108 (0/57)
2. Llevar **13 bicis** de 115 (21/23) a 256 (0/20)
3. Llevar **7 bicis** de 113 (13/13) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

171 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.123 | 0.036 |
| Sin resincronizar | 0.276 | 0.091 |
| Persistencia | 0.331 | 0.069 |
| Persistencia 0/1 | 0.331 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
