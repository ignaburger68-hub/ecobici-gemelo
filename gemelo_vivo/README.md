# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 11:54 (hora de Ciudad de México).

## Último pronóstico: 21/11 11:54 a 12:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.5 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 28 / 29 | 0.00 | 0.90 | 23-29 |
| 555 Ribera de San Cosme - Insurg | 34 / 35 | 0.00 | 0.81 | 30-35 |
| 010 Reforma - Ramírez | 1 / 25 | 0.76 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.74 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 26 / 27 | 0.00 | 0.67 | 23-27 |
| 119 Turín-Abraham González | 1 / 28 | 0.65 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.54 | 0.00 | 0-10 |
| 450 Ramos Arizpe- Av México Teno | 28 / 30 | 0.00 | 0.53 | 26-30 |
| 116 Londres-Roma | 2 / 23 | 0.49 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 14 / 20 | 0.00 | 0.46 | 12-20 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (28/29) a 010 (1/25)
2. Llevar **9 bicis** de 555 (34/35) a 020 (2/23)
3. Llevar **7 bicis** de 260 (14/20) a 085 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

319 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
