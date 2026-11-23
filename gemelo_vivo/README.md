# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 22:04 (hora de Ciudad de México).

## Último pronóstico: 22/11 22:04 a 23:04

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 5 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.98 | 30-33 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.68 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 1 / 17 | 0.67 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.60 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 1 / 11 | 0.43 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 23 / 27 | 0.00 | 0.35 | 22-27 |
| 115 Roma-Dinamarca | 3 / 25 | 0.21 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 2 / 15 | 0.18 | 0.00 | 1-5 |
| 119 Turín-Abraham González | 3 / 27 | 0.17 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 3 / 30 | 0.13 | 0.00 | 1-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 029 (33/33) a 003 (1/26)
2. Llevar **7 bicis** de 098 (23/27) a 008 (1/17)
3. Llevar **4 bicis** de 260 (14/19) a 086 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

433 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
