# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 09:16 (hora de Ciudad de México).

## Último pronóstico: 21/11 09:16 a 10:16

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.0 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.93** y las **devoluciones por 0.96** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 1 / 29 | 0.84 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 1 / 21 | 0.79 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 1 / 27 | 0.76 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.73 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 1 / 11 | 0.66 | 0.01 | 0-6 |
| 270 De la República-Ponciano Arr | 29 / 31 | 0.00 | 0.64 | 22-31 |
| 041 Reforma - Av. de la Repúblic | 2 / 28 | 0.63 | 0.00 | 1-13 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.52 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 3 / 15 | 0.51 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.48 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (29/31) a 119 (1/29)
2. Llevar **8 bicis** de 260 (15/21) a 112 (1/21)
3. Llevar **10 bicis** de 555 (24/34) a 041 (2/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

308 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
