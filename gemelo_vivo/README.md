# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 23:59 (hora de Ciudad de México).

## Último pronóstico: 22/11 22:48 a 23:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.5 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.99 | 31-33 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.98 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 11 | 0.54 | 0.00 | 0-2 |
| 008 Reforma - General Prim | 1 / 17 | 0.53 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 3 / 27 | 0.14 | 0.00 | 1-5 |
| 098 Emilio Dondé-Av. Balderas | 23 / 27 | 0.00 | 0.13 | 22-26 |
| 112 Av. Morelos-Abraham González | 3 / 20 | 0.07 | 0.00 | 1-5 |
| 117 Londres-Nápoles | 3 / 30 | 0.07 | 0.00 | 1-5 |
| 026 Reforma - Versalles | 4 / 11 | 0.05 | 0.00 | 1-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (33/33) a 003 (0/26)
2. Llevar **5 bicis** de 098 (23/27) a 086 (0/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

440 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
