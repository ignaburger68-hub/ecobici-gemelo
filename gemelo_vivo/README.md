# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 11:37 (hora de Ciudad de México).

## Último pronóstico: 22/11 11:37 a 12:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.1 mm/h · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.93** y las **devoluciones por 0.96** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 26 | 0.98 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.95 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 23 | 0.95 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.94 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.89 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 17 | 0.88 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.88 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 3 / 27 | 0.85 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (25/30) a 020 (1/21)
2. Llevar **15 bicis** de 259 (25/26) a 041 (5/29)
3. Llevar **13 bicis** de 107-108 (21/59) a 010 (3/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

389 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
