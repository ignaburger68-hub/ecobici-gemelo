# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 12:35 (hora de Ciudad de México).

## Último pronóstico: 22/11 12:35 a 13:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 116 Londres-Roma | 0 / 23 | 0.98 | 0.00 | 0-8 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.95 | 0.00 | 0-9 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.00 | 0.90 | 12-19 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.84 | 6-11 |
| 010 Reforma - Ramírez | 2 / 27 | 0.78 | 0.00 | 0-8 |
| 270 De la República-Ponciano Arr | 25 / 27 | 0.00 | 0.76 | 19-27 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.75 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 2 / 17 | 0.60 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.56 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 260 (18/19) a 116 (0/23)
2. Llevar **13 bicis** de 270 (25/27) a 010 (2/27)
3. Llevar **6 bicis** de 048 (10/11) a 115 (0/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

393 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
