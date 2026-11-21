# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 17:22 (hora de Ciudad de México).

## Último pronóstico: 21/11 17:22 a 18:22

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.3 °C** · sin lluvia · viento 6 km/h · día fin de semana

El clima multiplica los **retiros por 0.97** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 27 | 0.98 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 27 | 0.88 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.87 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 27 | 0.84 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 1 / 14 | 0.83 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.77 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 24 / 25 | 0.00 | 0.75 | 20-25 |
| 048 Independencia - Azueta | 8 / 9 | 0.05 | 0.72 | 2-9 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (32/34) a 041 (0/31)
2. Llevar **14 bicis** de 259 (24/25) a 115 (0/27)
3. Llevar **4 bicis** de 048 (8/9) a 020 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

342 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
