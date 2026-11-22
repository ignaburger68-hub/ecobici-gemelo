# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 14:43 (hora de Ciudad de México).

## Último pronóstico: 22/11 14:43 a 15:43

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
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.99 | 28-33 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.98 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.97 | 14-20 |
| 113 General Prim-Versalles | 0 / 15 | 0.97 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.96 | 5-11 |
| 116 Londres-Roma | 0 / 22 | 0.96 | 0.00 | 0-7 |
| 117 Londres-Nápoles | 0 / 30 | 0.95 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 1 / 23 | 0.80 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 27 / 28 | 0.00 | 0.78 | 19-27 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 029 (33/33) a 116 (0/22)
2. Llevar **10 bicis** de 260 (20/20) a 008 (0/16)
3. Llevar **12 bicis** de 270 (26/28) a 256 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

402 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
