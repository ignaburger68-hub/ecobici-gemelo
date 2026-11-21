# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 08:34 (hora de Ciudad de México).

## Último pronóstico: 21/11 08:34 a 09:34

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
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.77 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 22 | 0.67 | 0.00 | 1-10 |
| 115 Roma-Dinamarca | 1 / 27 | 0.62 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 3 / 34 | 0.58 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 1 / 15 | 0.56 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 2 / 11 | 0.47 | 0.01 | 0-7 |
| 026 Reforma - Versalles | 2 / 13 | 0.40 | 0.01 | 1-8 |
| 020 Reforma- Río Támesis | 3 / 22 | 0.36 | 0.00 | 1-10 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.35 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 4 / 29 | 0.32 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (15/20) a 112 (1/21)
2. Llevar **9 bicis** de 270 (20/27) a 255 (3/34)
3. Llevar **6 bicis** de 029 (22/33) a 116 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

305 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
