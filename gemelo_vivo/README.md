# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 08:48 (hora de Ciudad de México).

## Último pronóstico: 21/11 08:48 a 09:48

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
| 115 Roma-Dinamarca | 0 / 27 | 0.96 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 1 / 11 | 0.66 | 0.01 | 0-7 |
| 119 Turín-Abraham González | 2 / 29 | 0.60 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 1 / 15 | 0.55 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 16 / 20 | 0.00 | 0.54 | 14-20 |
| 116 Londres-Roma | 1 / 23 | 0.52 | 0.00 | 1-10 |
| 112 Av. Morelos-Abraham González | 2 / 21 | 0.49 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 4 / 34 | 0.43 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 3 / 22 | 0.34 | 0.00 | 1-11 |
| 008 Reforma - General Prim | 3 / 16 | 0.29 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 260 (16/20) a 115 (0/27)
2. Llevar **10 bicis** de 029 (21/33) a 119 (2/29)
3. Llevar **8 bicis** de 270 (19/28) a 112 (2/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

306 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
