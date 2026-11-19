# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 16:53 (hora de Ciudad de México).

## Último pronóstico: 19/11 16:53 a 17:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 11 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 10-15 km/h | 0.862 | 0.898 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 27 | 1.00 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 17 / 17 | 0.00 | 0.99 | 10-17 |
| 020 Reforma- Río Támesis | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 13 | 0.98 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.97 | 0.00 | 0-6 |
| 098 Emilio Dondé-Av. Balderas | 0 / 29 | 0.97 | 0.00 | 1-8 |
| 270 De la República-Ponciano Arr | 0 / 22 | 0.96 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.96 | 0.01 | 1-9 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 114 (17/17) a 010 (0/27)
2. Llevar **10 bicis** de 116 (13/17) a 031 (2/30)
3. Llevar **7 bicis** de 260 (9/20) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

198 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.121 | 0.036 |
| Sin resincronizar | 0.297 | 0.095 |
| Persistencia | 0.336 | 0.069 |
| Persistencia 0/1 | 0.336 | 0.069 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
