# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 13:32 (hora de Ciudad de México).

## Último pronóstico: 22/11 13:32 a 14:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.1 °C** · lluvia 0.2 mm/h · viento 5 km/h · día fin de semana

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 27 | 0.99 | 0.00 | 0-6 |
| 117 Londres-Nápoles | 0 / 30 | 0.98 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 0 / 36 | 0.97 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 0 / 28 | 0.97 | 0.00 | 0-7 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.97 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.95 | 12-20 |
| 098 Emilio Dondé-Av. Balderas | 0 / 26 | 0.94 | 0.00 | 0-8 |
| 115 Roma-Dinamarca | 1 / 26 | 0.86 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 32 / 33 | 0.00 | 0.85 | 27-33 |
| 012 Río Lerma - Villalongín | 1 / 11 | 0.83 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 029 (32/33) a 010 (0/27)
2. Llevar **11 bicis** de 260 (20/20) a 031 (0/36)
3. Llevar **12 bicis** de 041 (26/29) a 003 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

397 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
