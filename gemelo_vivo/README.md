# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 11:23 (hora de Ciudad de México).

## Último pronóstico: 22/11 11:23 a 12:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.9 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.95** y las **devoluciones por 0.98** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 23 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 12 | 0.99 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 20 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.96 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 2 / 27 | 0.92 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 270 (28/30) a 041 (1/29)
2. Llevar **15 bicis** de 259 (25/26) a 020 (0/20)
3. Llevar **14 bicis** de 107-108 (23/58) a 116 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

388 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
