# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 21:50 (hora de Ciudad de México).

## Último pronóstico: 22/11 21:50 a 22:50

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
| 048 Independencia - Azueta | 0 / 11 | 0.98 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.80 | 30-33 |
| 008 Reforma - General Prim | 1 / 17 | 0.66 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 1 / 15 | 0.44 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 2 / 26 | 0.34 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.33 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.29 | 0.01 | 0-7 |
| 098 Emilio Dondé-Av. Balderas | 23 / 27 | 0.00 | 0.27 | 22-27 |
| 115 Roma-Dinamarca | 3 / 25 | 0.21 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 3 / 27 | 0.12 | 0.00 | 1-5 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (32/33) a 008 (1/17)
2. Llevar **5 bicis** de 098 (23/27) a 048 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

432 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
