# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 21:07 (hora de Ciudad de México).

## Último pronóstico: 22/11 21:07 a 22:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.2 °C** · sin lluvia · viento 5 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.01 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.98 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.97 | 28-33 |
| 008 Reforma - General Prim | 1 / 17 | 0.86 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.73 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 15 | 0.63 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 2 / 11 | 0.52 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 2 / 30 | 0.33 | 0.00 | 0-6 |
| 003 Reforma - Insurgentes | 4 / 27 | 0.29 | 0.00 | 1-8 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (33/33) a 010 (0/26)
2. Llevar **8 bicis** de 260 (15/19) a 008 (1/17)
3. Llevar **6 bicis** de 098 (22/27) a 026 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

429 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
