# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 10:15 (hora de Ciudad de México).

## Último pronóstico: 21/11 10:15 a 11:15

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**19.1 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 0.99** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 22 | 0.98 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 29 / 29 | 0.00 | 0.97 | 22-29 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.83 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 27 | 0.72 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.63 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 31 | 0.54 | 0.00 | 1-15 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.53 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 3 / 29 | 0.51 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 2 / 15 | 0.51 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.43 | 0.00 | 1-11 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (29/29) a 112 (0/22)
2. Llevar **6 bicis** de 260 (13/21) a 085 (1/15)
3. Llevar **7 bicis** de 012 (11/15) a 041 (3/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

312 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
