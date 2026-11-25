# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 25/11/2026 06:37 (hora de Ciudad de México).

## Último pronóstico: 25/11 06:37 a 07:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.9 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 114 Lucerna-Abraham González | 0 / 23 | 1.00 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 098 Emilio Dondé-Av. Balderas | 0 / 15 | 0.99 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 0 / 25 | 0.99 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 0 / 15 | 0.98 | 0.00 | 0-5 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.96 | 18-26 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.70 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 3 / 30 | 0.54 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 2 / 15 | 0.48 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (27/27) a 086 (0/14)
2. Llevar **12 bicis** de 119 (27/29) a 114 (0/23)
3. Llevar **9 bicis** de 259 (20/24) a 041 (3/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

582 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.239 | 0.083 |
| Persistencia | 0.267 | 0.061 |
| Persistencia 0/1 | 0.267 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
