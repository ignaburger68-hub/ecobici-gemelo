# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 15:11 (hora de Ciudad de México).

## Último pronóstico: 22/11 15:11 a 16:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.9 °C** · lluvia 0.3 mm/h · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.82** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.98 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.98 | 28-33 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.97 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 0 / 30 | 0.97 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 18 | 0.00 | 0.97 | 13-18 |
| 112 Av. Morelos-Abraham González | 20 / 20 | 0.00 | 0.96 | 14-20 |
| 270 De la República-Ponciano Arr | 26 / 27 | 0.00 | 0.86 | 21-27 |
| 048 Independencia - Azueta | 9 / 10 | 0.01 | 0.78 | 5-10 |
| 114 Lucerna-Abraham González | 1 / 23 | 0.67 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (26/27) a 256 (0/23)
2. Llevar **8 bicis** de 260 (18/18) a 085 (0/13)
3. Llevar **15 bicis** de 029 (33/33) a 117 (0/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

404 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
