# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 09:02 (hora de Ciudad de México).

## Último pronóstico: 21/11 09:02 a 10:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.0 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.75 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 27 | 0.67 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 1 / 11 | 0.62 | 0.01 | 0-6 |
| 119 Turín-Abraham González | 2 / 29 | 0.61 | 0.00 | 0-5 |
| 116 Londres-Roma | 1 / 23 | 0.59 | 0.00 | 1-9 |
| 260 Av. Juárez-Balderas | 16 / 20 | 0.00 | 0.55 | 14-20 |
| 085 Rosas Moreno - Sullivan | 3 / 15 | 0.51 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 2 / 15 | 0.47 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 4 / 23 | 0.33 | 0.00 | 0-11 |
| 041 Reforma - Av. de la Repúblic | 4 / 30 | 0.25 | 0.00 | 1-14 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 260 (16/20) a 112 (1/21)
2. Llevar **9 bicis** de 270 (22/29) a 119 (2/29)
3. Llevar **11 bicis** de 450 (24/29) a 115 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

307 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
