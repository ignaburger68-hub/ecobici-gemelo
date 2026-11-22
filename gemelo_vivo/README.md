# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 12:06 (hora de Ciudad de México).

## Último pronóstico: 22/11 12:06 a 13:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.1 mm/h · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 13-20 |
| 020 Reforma- Río Támesis | 0 / 20 | 0.97 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 25 | 0.00 | 0.97 | 21-25 |
| 008 Reforma - General Prim | 0 / 17 | 0.97 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 0 / 35 | 0.95 | 0.00 | 0-8 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.94 | 0.00 | 1-8 |
| 010 Reforma - Ramírez | 3 / 27 | 0.75 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.74 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 3 / 27 | 0.69 | 0.01 | 1-14 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (20/20) a 020 (0/20)
2. Llevar **14 bicis** de 259 (25/25) a 010 (3/27)
3. Llevar **10 bicis** de 270 (24/29) a 008 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

391 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
