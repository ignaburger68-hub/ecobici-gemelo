# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 20:25 (hora de Ciudad de México).

## Último pronóstico: 22/11 20:25 a 21:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.8 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.74** y las **devoluciones por 0.79** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 22 | 0.99 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.98 | 26-33 |
| 008 Reforma - General Prim | 1 / 17 | 0.81 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.68 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 1 / 14 | 0.66 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.55 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 2 / 11 | 0.55 | 0.02 | 0-7 |
| 048 Independencia - Azueta | 2 / 11 | 0.43 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 4 / 26 | 0.29 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 029 (33/33) a 010 (0/26)
2. Llevar **8 bicis** de 259 (20/26) a 008 (1/17)
3. Llevar **5 bicis** de 029 (33/33) a 086 (1/12)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

426 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
