# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 21:39 (hora de Ciudad de México).

## Último pronóstico: 21/11 21:39 a 22:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.98 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 30 | 0.98 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 1 / 21 | 0.68 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 32 | 0.56 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 2 / 26 | 0.41 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 2 / 15 | 0.41 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 3 / 16 | 0.29 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 3 / 27 | 0.23 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 3 / 15 | 0.18 | 0.00 | 1-7 |
| 048 Independencia - Azueta | 3 / 11 | 0.13 | 0.00 | 1-6 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 450 (26/30) a 003 (0/30)
2. Llevar **12 bicis** de 259 (23/27) a 041 (2/32)
3. Llevar **9 bicis** de 555 (26/33) a 260 (1/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

360 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
