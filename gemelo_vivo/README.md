# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 08:05 (hora de Ciudad de México).

## Último pronóstico: 21/11 08:05 a 09:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 28 | 0.98 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 15 | 0.94 | 0.00 | 1-7 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.74 | 7-11 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.66 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 1 / 22 | 0.55 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 12 | 0.54 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 22 | 0.52 | 0.00 | 1-9 |
| 115 Roma-Dinamarca | 1 / 27 | 0.48 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 2 / 22 | 0.41 | 0.00 | 1-8 |
| 255 José Rosas Moreno-Guillermo  | 3 / 33 | 0.37 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 048 (10/11) a 119 (0/28)
2. Llevar **7 bicis** de 260 (12/18) a 112 (1/20)
3. Llevar **5 bicis** de 270 (16/26) a 113 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

303 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
