# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 20:43 (hora de Ciudad de México).

## Último pronóstico: 21/11 20:43 a 21:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.5 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.95** y las **devoluciones por 0.98** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 16 | 0.97 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 15 | 0.97 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.85 | 0.00 | 0-8 |
| 010 Reforma - Ramírez | 1 / 27 | 0.71 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 2 / 20 | 0.42 | 0.00 | 0-8 |
| 115 Roma-Dinamarca | 3 / 27 | 0.34 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 4 / 31 | 0.27 | 0.00 | 1-10 |
| 048 Independencia - Azueta | 8 / 11 | 0.01 | 0.19 | 5-10 |
| 086 Sullivan-Insurgentes | 10 / 15 | 0.00 | 0.12 | 7-14 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 450 (26/30) a 041 (1/32)
2. Llevar **7 bicis** de 270 (26/32) a 008 (0/16)
3. Llevar **7 bicis** de 259 (24/27) a 026 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

356 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
