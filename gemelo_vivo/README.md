# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 15:14 (hora de Ciudad de México).

## Último pronóstico: 21/11 15:14 a 16:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.5 °C** · sin lluvia · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.98 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.95 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 15 | 0.81 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 27 | 0.79 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 2 / 27 | 0.70 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.69 | 13-20 |
| 116 Londres-Roma | 2 / 23 | 0.69 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.69 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **18 bicis** de 031 (33/35) a 041 (1/31)
2. Llevar **8 bicis** de 260 (19/20) a 086 (0/15)
3. Llevar **8 bicis** de 555 (30/34) a 012 (0/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

333 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
