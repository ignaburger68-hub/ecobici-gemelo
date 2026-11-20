# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 12:54 (hora de Ciudad de México).

## Último pronóstico: 20/11 12:54 a 13:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 1.00 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 23 / 23 | 0.00 | 0.99 | 18-23 |
| 555 Ribera de San Cosme - Insurg | 1 / 34 | 0.92 | 0.00 | 1-8 |
| 117 Londres-Nápoles | 29 / 30 | 0.00 | 0.91 | 24-30 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.89 | 6-10 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.84 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.80 | 12-19 |
| 031 Hamburgo - Insurgentes | 33 / 34 | 0.00 | 0.78 | 27-34 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 116 (23/23) a 555 (1/34)
2. Llevar **13 bicis** de 117 (29/30) a 256 (0/23)
3. Llevar **15 bicis** de 031 (33/34) a 041 (2/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

252 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.275 | 0.091 |
| Persistencia | 0.315 | 0.065 |
| Persistencia 0/1 | 0.315 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
