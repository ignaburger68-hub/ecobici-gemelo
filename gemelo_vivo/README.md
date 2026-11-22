# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 12:49 (hora de Ciudad de México).

## Último pronóstico: 22/11 12:49 a 13:49

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · lluvia 0.1 mm/h · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 30 | 0.98 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 0 / 26 | 0.97 | 0.00 | 0-5 |
| 008 Reforma - General Prim | 0 / 15 | 0.97 | 0.00 | 0-7 |
| 031 Hamburgo - Insurgentes | 0 / 36 | 0.96 | 0.00 | 0-8 |
| 116 Londres-Roma | 0 / 23 | 0.96 | 0.00 | 0-9 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.95 | 0.00 | 0-9 |
| 048 Independencia - Azueta | 10 / 11 | 0.01 | 0.85 | 6-11 |
| 003 Reforma - Insurgentes | 1 / 29 | 0.79 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.74 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 17 / 20 | 0.00 | 0.62 | 11-20 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 260 (17/20) a 020 (0/22)
2. Llevar **6 bicis** de 048 (10/11) a 117 (0/30)
3. Llevar **11 bicis** de 270 (23/28) a 031 (0/36)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

394 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
