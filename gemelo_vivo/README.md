# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 13:04 (hora de Ciudad de México).

## Último pronóstico: 22/11 13:03 a 14:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 0 / 26 | 0.98 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.97 | 13-20 |
| 119 Turín-Abraham González | 0 / 28 | 0.97 | 0.00 | 0-8 |
| 031 Hamburgo - Insurgentes | 1 / 36 | 0.77 | 0.00 | 0-8 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.74 | 0.00 | 0-8 |
| 117 Londres-Nápoles | 1 / 30 | 0.71 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.70 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 23 | 0.65 | 0.00 | 1-10 |
| 041 Reforma - Av. de la Repúblic | 23 / 29 | 0.00 | 0.62 | 19-29 |
| 010 Reforma - Ramírez | 2 / 26 | 0.61 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 260 (20/20) a 115 (0/26)
2. Llevar **14 bicis** de 041 (23/29) a 031 (1/36)
3. Llevar **11 bicis** de 270 (22/28) a 119 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

395 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
