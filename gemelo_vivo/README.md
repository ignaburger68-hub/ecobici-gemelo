# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 14:31 (hora de Ciudad de México).

## Último pronóstico: 21/11 14:30 a 15:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.5 °C** · sin lluvia · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.97** y las **devoluciones por 1.01** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.97 | 13-20 |
| 048 Independencia - Azueta | 10 / 10 | 0.04 | 0.95 | 3-10 |
| 555 Ribera de San Cosme - Insurg | 34 / 34 | 0.00 | 0.92 | 23-33 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.92 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 14 | 0.83 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 1 / 27 | 0.82 | 0.00 | 0-5 |
| 116 Londres-Roma | 1 / 23 | 0.82 | 0.00 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.77 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 30 / 31 | 0.00 | 0.77 | 22-31 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.68 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (20/20) a 041 (1/31)
2. Llevar **14 bicis** de 555 (34/34) a 010 (1/27)
3. Llevar **12 bicis** de 270 (30/31) a 116 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

330 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
