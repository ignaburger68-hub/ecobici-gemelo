# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 14:14 (hora de Ciudad de México).

## Último pronóstico: 22/11 14:14 a 15:14

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.1 °C** · lluvia 0.2 mm/h · viento 5 km/h · día fin de semana

El clima multiplica los **retiros por 0.82** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-4 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.98 | 28-33 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.98 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 11 / 11 | 0.03 | 0.97 | 4-11 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.96 | 13-20 |
| 117 Londres-Nápoles | 0 / 30 | 0.96 | 0.00 | 0-7 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.96 | 0.03 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 27 / 27 | 0.00 | 0.96 | 17-26 |
| 116 Londres-Roma | 1 / 23 | 0.85 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 029 (33/33) a 256 (0/23)
2. Llevar **10 bicis** de 041 (27/27) a 118 (0/16)
3. Llevar **10 bicis** de 260 (20/20) a 116 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

400 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
