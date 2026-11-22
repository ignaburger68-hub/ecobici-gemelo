# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 13:18 (hora de Ciudad de México).

## Último pronóstico: 22/11 13:18 a 14:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.5 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.98 | 5-11 |
| 115 Roma-Dinamarca | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.97 | 13-20 |
| 119 Turín-Abraham González | 0 / 28 | 0.97 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 0 / 36 | 0.96 | 0.00 | 0-8 |
| 116 Londres-Roma | 0 / 23 | 0.95 | 0.00 | 0-8 |
| 041 Reforma - Av. de la Repúblic | 27 / 29 | 0.00 | 0.83 | 20-29 |
| 010 Reforma - Ramírez | 1 / 27 | 0.82 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.58 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 3 / 12 | 0.56 | 0.03 | 0-8 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 041 (27/29) a 031 (0/36)
2. Llevar **10 bicis** de 260 (20/20) a 115 (0/26)
3. Llevar **6 bicis** de 048 (11/11) a 010 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

396 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
