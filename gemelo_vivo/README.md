# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 17:37 (hora de Ciudad de México).

## Último pronóstico: 21/11 17:36 a 18:36

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.97** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 0 / 23 | 0.98 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.83 | 22-32 |
| 115 Roma-Dinamarca | 1 / 27 | 0.78 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 2 / 27 | 0.57 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.51 | 0.01 | 0-7 |
| 098 Emilio Dondé-Av. Balderas | 3 / 27 | 0.51 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 031 (32/33) a 041 (0/31)
2. Llevar **12 bicis** de 259 (22/25) a 020 (0/23)
3. Llevar **11 bicis** de 555 (27/33) a 010 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

343 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
