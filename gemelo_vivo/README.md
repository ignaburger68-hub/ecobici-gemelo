# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 21:25 (hora de Ciudad de México).

## Último pronóstico: 21/11 21:25 a 22:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.83 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 1 / 16 | 0.80 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.77 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.74 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 31 | 0.73 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 3 / 21 | 0.33 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 3 / 15 | 0.30 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 4 / 15 | 0.12 | 0.00 | 1-7 |
| 048 Independencia - Azueta | 4 / 11 | 0.11 | 0.00 | 1-7 |
| 113 General Prim-Versalles | 3 / 15 | 0.10 | 0.00 | 1-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 259 (24/27) a 041 (1/32)
2. Llevar **8 bicis** de 270 (23/31) a 008 (1/16)
3. Llevar **9 bicis** de 450 (25/30) a 003 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

359 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
