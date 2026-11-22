# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 15:25 (hora de Ciudad de México).

## Último pronóstico: 22/11 15:25 a 16:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.9 °C** · lluvia 0.3 mm/h · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.80** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 18 / 18 | 0.00 | 0.99 | 14-18 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.98 | 7-11 |
| 008 Reforma - General Prim | 0 / 16 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.98 | 7-11 |
| 112 Av. Morelos-Abraham González | 20 / 20 | 0.00 | 0.98 | 15-20 |
| 115 Roma-Dinamarca | 0 / 25 | 0.97 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.96 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.81 | 29-33 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 26 | 0.00 | 0.80 | 23-26 |
| 270 De la República-Ponciano Arr | 26 / 28 | 0.00 | 0.78 | 23-28 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (18/18) a 115 (0/25)
2. Llevar **14 bicis** de 270 (26/28) a 256 (0/23)
3. Llevar **10 bicis** de 029 (32/33) a 008 (0/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

405 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
