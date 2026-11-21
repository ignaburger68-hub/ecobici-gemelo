# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 10:29 (hora de Ciudad de México).

## Último pronóstico: 21/11 10:29 a 11:29

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
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.82 | 0.00 | 1-13 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.80 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 27 | 0.72 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 15 | 0.71 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.67 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 27 / 29 | 0.00 | 0.59 | 21-29 |
| 048 Independencia - Azueta | 1 / 11 | 0.59 | 0.01 | 0-6 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.49 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (27/29) a 116 (0/22)
2. Llevar **8 bicis** de 012 (12/15) a 041 (1/31)
3. Llevar **12 bicis** de 450 (25/30) a 255 (0/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

313 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
