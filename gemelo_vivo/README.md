# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 09:15 (hora de Ciudad de México).

## Último pronóstico: 22/11 09:14 a 10:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.8 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-2 |
| 041 Reforma - Av. de la Repúblic | 0 / 30 | 0.99 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 0 / 33 | 0.97 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 0 / 27 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.77 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 15 | 0.74 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.72 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 3 / 21 | 0.65 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 2 / 30 | 0.49 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 3 / 26 | 0.44 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 259 (24/26) a 041 (0/30)
2. Llevar **13 bicis** de 555 (24/33) a 029 (0/33)
3. Llevar **10 bicis** de 107-108 (22/58) a 008 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

379 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
