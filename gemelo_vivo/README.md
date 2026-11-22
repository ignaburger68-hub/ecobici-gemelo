# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 14:57 (hora de Ciudad de México).

## Último pronóstico: 22/11 14:57 a 15:57

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
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 1.00 | 28-33 |
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 14-20 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.96 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 26 / 27 | 0.00 | 0.86 | 21-27 |
| 112 Av. Morelos-Abraham González | 19 / 20 | 0.00 | 0.81 | 14-20 |
| 116 Londres-Roma | 1 / 22 | 0.75 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 9 / 10 | 0.01 | 0.75 | 5-10 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.69 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.67 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 029 (33/33) a 008 (0/16)
2. Llevar **12 bicis** de 270 (26/27) a 116 (1/22)
3. Llevar **8 bicis** de 260 (20/20) a 118 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

403 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
