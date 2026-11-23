# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 13:06 (hora de Ciudad de México).

## Último pronóstico: 23/11 13:06 a 14:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.1 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 12 | 0.98 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.97 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.96 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 27 | 0.88 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 1 / 27 | 0.86 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 16 | 0.84 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 117 (25/29) a 555 (0/29)
2. Llevar **11 bicis** de 115 (19/25) a 041 (1/32)
3. Llevar **9 bicis** de 450 (13/30) a 260 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

466 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.291 | 0.063 |
| Persistencia 0/1 | 0.291 | 0.063 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
