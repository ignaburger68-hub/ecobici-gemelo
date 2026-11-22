# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 15:39 (hora de Ciudad de México).

## Último pronóstico: 22/11 15:39 a 16:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.76** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.98 | 6-11 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.97 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.96 | 0.00 | 0-5 |
| 116 Londres-Roma | 0 / 23 | 0.96 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 0 / 27 | 0.95 | 0.00 | 1-8 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.84 | 29-33 |
| 270 De la República-Ponciano Arr | 26 / 28 | 0.00 | 0.75 | 23-28 |
| 115 Roma-Dinamarca | 1 / 25 | 0.72 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 15 | 0.71 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.69 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (26/28) a 003 (0/29)
2. Llevar **11 bicis** de 029 (32/33) a 116 (0/23)
3. Llevar **6 bicis** de 048 (11/11) a 256 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

406 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
